# Generated by Django 3.1.5 on 2021-02-02 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager', '0003_student_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='max_student',
            new_name='max_students',
        ),
    ]
