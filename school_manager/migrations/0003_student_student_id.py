# Generated by Django 3.1.5 on 2021-02-02 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager', '0002_remove_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
