# Generated by Django 3.1.7 on 2021-03-24 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('khana', '0007_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
