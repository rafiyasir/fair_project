# Generated by Django 2.2.7 on 2019-12-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='about_content_3',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
