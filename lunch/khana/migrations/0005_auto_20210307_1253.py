# Generated by Django 3.1.7 on 2021-03-07 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('khana', '0004_auto_20210304_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='person_id',
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]