# Generated by Django 4.1.1 on 2022-11-28 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_1', '0004_tag_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_name',
            new_name='image',
        ),
    ]