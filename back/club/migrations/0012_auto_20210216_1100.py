# Generated by Django 3.1.3 on 2021-02-16 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_club_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club_article',
            old_name='decription',
            new_name='description',
        ),
    ]
