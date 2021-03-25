from .models import Test, TempUser
import datetime
from django.utils import timezone


def my_scheduled_job():
    Test.objects.create(name='test')


def expire_temp_user():
    TempUser.objects.filter(created__lt=timezone.now() - datetime.timedelta(days=2)).delete()
