# Generated by Django 4.1.7 on 2023-05-10 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cricket_Question_and_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_Technology_Waves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField()),
                ('output', models.TextField(blank=True, null=True)),
                ('variant', models.CharField(choices=[('1 variant', '1 variant'), ('2 variant', '2 variant'), ('3 variant', '3 variant')], max_length=30)),
                ('language', models.CharField(choices=[('en', 'english'), ('af', 'afrikaans'), ('sq', 'albanian'), ('am', 'amharic'), ('ar', 'arabic'), ('hy', 'armenian'), ('az', 'azerbaijani'), ('eu', 'basque'), ('be', 'belarusian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('bg', 'bulgarian'), ('ca', 'catalan'), ('ceb', 'cebuano'), ('ny', 'chichewa'), ('zh-cn', 'chinese (simplified)'), ('zh-tw', 'chinese (traditional)'), ('co', 'corsican'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('eo', 'esperanto'), ('et', 'estonian'), ('tl', 'filipino'), ('fi', 'finnish'), ('fr', 'french'), ('fy', 'frisian'), ('gl', 'galician'), ('ka', 'georgian'), ('de', 'german'), ('el', 'greek'), ('gu', 'gujarati'), ('ht', 'haitian creole'), ('ha', 'hausa'), ('haw', 'hawaiian'), ('hi', 'hindi'), ('hmn', 'hmong'), ('hu', 'hungarian'), ('is', 'icelandic'), ('ig', 'igbo'), ('id', 'indonesian'), ('ga', 'irish'), ('it', 'italian'), ('ja', 'japanese'), ('jw', 'javanese'), ('kn', 'kannada'), ('kk', 'kazakh'), ('km', 'khmer'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('lo', 'lao'), ('la', 'latin'), ('lv', 'latvian'), ('lt', 'lithuanian'), ('lb', 'luxembourgish'), ('mk', 'macedonian'), ('mg', 'malagasy'), ('ms', 'malay'), ('ml', 'malayalam'), ('mt', 'maltese'), ('mi', 'maori'), ('mr', 'marathi'), ('mn', 'mongolian'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('no', 'norwegian'), ('ps', 'pashto'), ('fa', 'persian'), ('pl', 'polish'), ('pt', 'portuguese'), ('pa', 'punjabi'), ('ro', 'romanian'), ('ru', 'russian'), ('sm', 'samoan'), ('gd', 'scots gaelic'), ('sr', 'serbian'), ('st', 'sesotho'), ('sn', 'shona'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('so', 'somali'), ('es', 'spanish'), ('su', 'sundanese'), ('sw', 'swahili'), ('sv', 'swedish'), ('tg', 'tajik'), ('ta', 'tamil'), ('te', 'telugu'), ('th', 'thai'), ('tr', 'turkish'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('cy', 'welsh'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zu', 'zulu'), ('he', 'Hebrew'), ('fil', 'Filipino')], max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
