# Generated by Django 4.2.10 on 2024-03-16 02:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscription',
            field=models.ManyToManyField(related_name='category', through='news.Subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]