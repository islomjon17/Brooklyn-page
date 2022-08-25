# Generated by Django 4.1 on 2022-08-25 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0002_speakingpart2'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakingPartThreeTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='speakingpart3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=255)),
                ('answer1', models.TextField()),
                ('question2', models.CharField(blank=True, max_length=255)),
                ('answer2', models.TextField(blank=True)),
                ('question3', models.CharField(blank=True, max_length=255)),
                ('answer3', models.TextField(blank=True)),
                ('question4', models.CharField(blank=True, max_length=255)),
                ('answer4', models.TextField(blank=True)),
                ('question5', models.CharField(blank=True, max_length=255)),
                ('answer5', models.TextField(blank=True)),
                ('question6', models.CharField(blank=True, max_length=255)),
                ('answer6', models.TextField(blank=True)),
                ('question7', models.CharField(blank=True, max_length=255)),
                ('answer7', models.TextField(blank=True)),
                ('question8', models.CharField(blank=True, max_length=255)),
                ('answer8', models.TextField(blank=True)),
                ('topic', models.ForeignKey(default='unnamed', on_delete=django.db.models.deletion.CASCADE, to='ielts.speakingpartthreetopic')),
            ],
        ),
    ]