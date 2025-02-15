# Generated by Django 4.2.4 on 2023-09-03 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('quiz', '0003_question_option10_question_option5_question_option6_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel'),
        ),
        migrations.AddField(
            model_name='course',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=150, null=True, unique=True),
        ),
    ]
