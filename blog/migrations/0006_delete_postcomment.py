# Generated by Django 4.0.3 on 2022-03-12 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_add_date_alter_category_add_date_postcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]
