# Generated by Django 4.2.1 on 2023-09-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_leadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadfile',
            name='file',
            field=models.FileField(upload_to='leadtfiles'),
        ),
    ]
