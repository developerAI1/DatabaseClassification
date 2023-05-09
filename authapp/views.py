from .models import *
from .models import LANGUAGE_CHOICES
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from authapp.renderer import UserRenderer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.views import APIView
from distutils import errors
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
import openai
import googletrans
from googletrans import Translator
from django.conf import settings
from bs4 import BeautifulSoup
import requests
import re

translator = Translator()
openai.api_key=settings.API_KEY

#Creating tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
 renderer_classes=[UserRenderer]
 def post(self,request,format=None):
    serializer=UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user=serializer.save()
        return Response({'message':'Registation successful',"status":"status.HTTP_200_OK"})
    return Response({errors:serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 
class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(email=email,password=password)
        
        if user is not None:
              token= get_tokens_for_user(user)
              return Response({'message':'Login successful','status':'status.HTTP_200_OK',"token":token})
        else:
              return Response({'message':'Please Enter Valid email or password',"status":"status.HTTP_404_NOT_FOUND"})

class LogoutUser(APIView):
  renderer_classes = [UserRenderer]
  permission_classes=[IsAuthenticated]
  def post(self, request, format=None):
    return Response({'message':'Logout Successfully','status':'status.HTTP_200_OK'})


class ContenViews(APIView):
    renderer_classes=[UserRenderer]  
    def post(self,request):
        input=request.data.get('input')
        language=request.data.get('language')
        variant=request.data.get('variant')
        user_id=request.data.get('user_id')
        if not input:
            return Response({"message":"please provide input text"})
        if not language:
            return Response({"message":"please select langusge"})
        if not variant:
            return Response({"message":"select variant for creativity"})
        if not user_id:
            return Response({"message":"user is required"})
        if not User.objects.filter(id=user_id).exists():
             return Response({"message":" user does not exist"})
         
        user=User.objects.get(id=user_id)
        user.user=user
        content_data=Content.objects.create(input=input,language=language,user_id=user,variant=variant)
        serializers=ContentSerializer(data=content_data)
        content_data.save()
        
#### get data from the database
       
        input_text=content_data.input                   ## get input data from the database.
        language_detect=content_data.language           ## get language from the database
        variant_data=content_data.variant               ## get variant option detect from the database
        content_id=content_data.id
        
        if variant=="1 variant":
            loops=1
        elif variant=="2 variant":
            loops=2
        elif variant=="3 variant":
            loops=3
        else:
            return Response ({"message":"Invalid varinat value"})
        
        outputs=[]
        for i in range(loops):
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Auto Response Generator \n\nUser: {input_text} \n\nAI:\n",
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=1,    
            presence_penalty=1,
            )   
            output= response.choices[0].text
            translated_output = translator.translate(output, dest=language_detect).text
            outputs.append(translated_output)
        update_content=Content.objects.filter(id=content_id).update(output=outputs)
        return Response({'msg':'Data Added Succesfully','status':'status.HTTP_201_CREATED','output':outputs})   
class CricketScrapingView(APIView):
	def post(self, request, format=None):
    	     urls = ["https://www.prep4ias.com/top-300-cricket-general-knowledge-questions-and-answers/","https://www.edubabaji.com/top-50-cricket-gk-questions-answers-in-english/"]
    	     array=[]
    	     for index, url in enumerate(urls):
	         if index ==0:
    #                 print(url)

	                 response = requests.get(url)
	                 html_content = response.content
    	                 soup = BeautifulSoup(html_content, "html.parser")
	                 pattern = r'^\d{1,2}\b'
    	                 h3_tags = soup.find_all("h3")
    	                 count = 0
    	                 for h3 in h3_tags:
   	                     if count == 60:
    	                         break
    	                     question=h3.text
   	                     question=re.sub(r'\.', '', question)
    	                     question=re.sub(r'\d+', '', question)
    #                     # print(question)
    	                     answer=h3.find_next("p").text
   	                     answer=re.sub(r'\.', '', answer)
    	                     answer= re.sub(r'\bAns\b', '', answer)
    	                     data_dict={"question":question,"answer":answer}
    	                     array.append(data_dict)
    #                     # print(array)
    	                     count += 1
             if index ==1:
    	#                 print(url)
                     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

                     response = requests.get(url,headers=headers)

                     soup = BeautifulSoup(response.content, "html.parser")

                     video_wrapper = soup.find("div", {"class": "jetpack-video-wrapper"})

                     ol_tag = soup.find('ol')

                     for li_tag in ol_tag.find_all('li'):
                         li_text = li_tag.text.strip()
                         strong_tag = li_tag.find('strong')
                         if strong_tag:
                             strong_text = strong_tag.text.strip()
                         else:
                             strong_text = None
                        
                         question=li_text
                         question=question.split('?')[0] + '?'
                         # print(question)

                         answer=strong_text
                         answer=answer[1:]
                         # print(answer)
                         data_dict2={"question":question,"answer":answer}
                         array.append(data_dict2)
         for x in array:
    #         print(x)
             question=(x['question'])
             answer=(x['answer'])
             cricketdata=Cricket_Question_and_Answer.objects.create(question=question,answer=answer)
             serializer=CricketSerializer(data=cricketdata)
             cricketdata.save()
         return Response({"message":"scrap data successfully","status":"200","data":"ok"})
    
class WebScrapDataView(APIView):
      def get(self, request, format=None):
         page = requests.get("https://buildfire.com/mobile-technology-waves/")
         soup = BeautifulSoup(page.content, "html.parser")
         p_tags = soup.select("h2 + p")
         array=[]
         count=0
         pattern = r'\d+'
         for p_tag in p_tags:
             h2_tag = p_tag.previous_sibling.previous_sibling
             if h2_tag is not None and h2_tag.name == "h2":
                 print(h2_tag.text)
             print(p_tag.text)
             question = re.sub(pattern, '', h2_tag.text)
             answer=re.sub(pattern, '', p_tag.text)
             scrappy=Mobile_Technology_Waves.objects.create(question=question,answer=answer)
             serializers=Mobile_Technology_WavesSerializer(data=scrappy)
             scrappy.save()
             count+=1
             if count==23:
                 break
         return Response({"message":"scrap data successfully","status":"200","Data":array})


class TechnologyView(APIView):
    def get(self, request, format=None):
        page = requests.get("https://www.ishir.com/blog/55810/top-15-emerging-technology-trends-to-watch-in-2023-and-beyond.htm")
        soup = BeautifulSoup(page.content, "html.parser")
        h3_tags = soup.find_all('h3')
        array=[]
        pattern = r'^\d{1,2}\b'
        for h3 in h3_tags:
            h3_text = h3.text.strip()
            question=h3_text
            question= question.replace(".", "")
            question = re.sub(pattern, '', question)

            # find the first paragraph tag after the h3 tag and extract its text
            paragraph = h3.find_next('p')
            if paragraph is not None:
                paragraph_text = paragraph.text.strip()
                answer=paragraph_text
            scrappy=Technologies.objects.create(question=question,answer=answer) 
            dict_data={"question":question,"answer":answer}
            array.append(dict_data)
        print(array)
        return Response({"message":"scrap data successfully","status":"200","data":array})
