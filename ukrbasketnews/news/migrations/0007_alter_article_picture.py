# Generated by Django 3.2.9 on 2021-12-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
