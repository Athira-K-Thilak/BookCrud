# Generated by Django 5.1.4 on 2024-12-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=200),
        ),
    ]
