# Generated by Django 4.2.11 on 2024-04-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dccomics',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marvel',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
