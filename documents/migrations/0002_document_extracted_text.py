# Generated by Django 5.1.5 on 2025-01-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='extracted_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
