from rest_framework import serializers
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','firstname','lastname']

        extra_kwargs={
            'email': {'error_messages': {'required': "email is required",'blank':'please provide a email'}},
            'password': {'error_messages': {'required': "password is required",'blank':'please Enter a password'}},
            'firstname': {'error_messages': {'required': "firstname is required",'blank':'firstname could not blank'}},
            'lastname': {'error_messages': {'required': "lastname is required",'blank':'lastname could not blank'}},
          }
        
    def create(self, validated_data,):
       user=User.objects.create(
       email=validated_data['email'],
       firstname=validated_data['firstname'],
       lastname=validated_data['lastname'],)
       user.set_password(validated_data['password']) 
       user.save()
       return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','firstname','lastname','is_admin']    



class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Content
        fields="__all__"

 
class CricketSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cricket_Question_and_Answer
        fields = '__all__'
           
    def create(self, validate_data):
        return Cricket_Question_and_Answer.objects.create(**validate_data)
     
class Mobile_Technology_WavesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mobile_Technology_Waves
        fields = '__all__'
           
    def create(self, validate_data):
        return Mobile_Technology_Waves.objects.create(**validate_data)

     
class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Technologies
        fields = '__all__'
           
    def create(self, validate_data):
        return Technologies.objects.create(**validate_data)
    
    
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Content
        fields="__all__"

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Topic
        fields = '__all__'
           
    def create(self, validate_data):
        return Topic.objects.create(**validate_data)



class QuestionAndAnswrSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuestionAndAnswr
        fields = '__all__'
           
    def create(self, validate_data):
        return QuestionAndAnswr.objects.create(**validate_data)
    

class User_LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model= User_Label
        fields = '__all__'
           
    def create(self, validate_data):
        return User_Label.objects.create(**validate_data)
    
class User_PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model= User_PDF
        fields = '__all__'
           
    def create(self, validate_data):
        return User_PDF.objects.create(**validate_data)
