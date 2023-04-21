# Generated by Django 4.1.4 on 2023-04-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('mark_of_physics', models.IntegerField()),
                ('mark_of_chemistry', models.IntegerField()),
                ('mark_of_computerscience', models.IntegerField()),
            ],
        ),
    ]