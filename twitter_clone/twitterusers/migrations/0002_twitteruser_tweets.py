# Generated by Django 2.2.7 on 2019-12-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
        ('twitterusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='tweets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet'),
        ),
    ]
