# Generated by Django 4.2.4 on 2023-09-16 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('updated',)},
        ),
    ]
