# Generated by Django 4.1.3 on 2022-11-02 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
