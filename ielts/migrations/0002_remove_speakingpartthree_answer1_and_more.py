# Generated by Django 4.1 on 2022-08-28 10:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer5',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer6',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer7',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='answer8',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question6',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question7',
        ),
        migrations.RemoveField(
            model_name='speakingpartthree',
            name='question8',
        ),
        migrations.AddField(
            model_name='speakingpartthree',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
