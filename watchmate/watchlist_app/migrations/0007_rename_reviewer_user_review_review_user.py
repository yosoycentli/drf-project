# Generated by Django 4.2.9 on 2024-01-19 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_review_reviewer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewer_user',
            new_name='review_user',
        ),
    ]
