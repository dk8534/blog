# Generated by Django 4.1.3 on 2022-11-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deatail',
            field=models.TextField(blank=True),
        ),
    ]
