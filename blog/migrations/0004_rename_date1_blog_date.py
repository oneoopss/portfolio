# Generated by Django 4.1.7 on 2023-03-27 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_date_blog_date1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date1',
            new_name='date',
        ),
    ]
