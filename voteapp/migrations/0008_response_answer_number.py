# Generated by Django 5.0.2 on 2024-03-07 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0007_alter_response_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='answer_number',
            field=models.IntegerField(default=0),
        ),
    ]
