from urllib import request
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app.resp_base import response_ok
from .serializers import SubscriberSerializer
from .models import Subscriber
from datetime import datetime
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.shortcuts import render
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import json

# Create your views here.

def index(requset):
    return HttpResponse("Assslamualaikum.")

@api_view(['GET','POST'])
def subs_list(request):
    if request.method == 'GET':
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCreateSubsView(CreateAPIView, APIView):
    def get(self, request, format=None):
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
        return render(request, 'dash.html', res)
        
def dash(request):
    data = ListCreateSubsView()
    context = {
        'data': data.get(request),
    }
    return render( request, 'dash.html', context)

@shared_task
def send_email_task():
    d1 = ListCreateSubsView()
    data = d1.get(request)
    print("Mail666 sending.......")
    subject = 'welcome to Celery world'
    message = json.dumps(data)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['souba67@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return "Mail has been sent........"
