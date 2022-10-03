from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
import json

#model&serializer
from .serializers import SubscriberSerializer
from .models import Subscriber


def get():
    month = datetime.strftime(datetime.now(), "%m")
    year = datetime.strftime(datetime.now(), "%Y")

    today = datetime.today()
    datem = datetime(today.year, today.month, 1)

    subs_count_monthly = Subscriber.objects.filter(deleted_dates__isnull=True, status=1,created_dates__year=year, created_dates__month=month).count()

    unsubs_count_monthly = Subscriber.objects.filter(deleted_dates__isnull=True, status=0, deleted_dates__year=year, deleted_dates__month=month).count()

    obj = Subscriber.objects.filter(deleted_dates__isnull=True).all().order_by('-id')

    subs = [sub.serialize for sub in obj]
        
    res = {
            'subs_count_on_month': subs_count_monthly,
            'unsubs_count_on_month': unsubs_count_monthly,
            'total': obj.count(),
            'subslist': subs,
            'date': datem
        }
    return (res)

@shared_task
def send_email_task():
    a = get()
    print("Mail666 sending.......")
    subject = 'welcome to Celery world'
    message =  'This month report'+ '\n\n' + 'New subscriber this month: ' + json.dumps(a['subs_count_on_month']) + '\n\n' 'Unsubscribe count month: ' + json.dumps(a['unsubs_count_on_month'])  + '\n\n' 'Total subscriber: ' + json.dumps(a['total'])
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['souba67@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return "Mail has been sent........"