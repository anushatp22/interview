# Generated by Django 4.1.4 on 2023-04-20 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_student_tb_delete_student_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_tb',
            name='average',
        ),
    ]