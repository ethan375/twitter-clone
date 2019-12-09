# Generated by Django 2.2.7 on 2019-12-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterusers', '0003_auto_20191206_1520'),
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='twitterusers.TwitterUser'),
            preserve_default=False,
        ),
    ]
