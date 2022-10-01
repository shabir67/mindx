from django.urls import path
from .views import ListCreateSubsView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriber', views.subs_list),
    path('dash', ListCreateSubsView.as_view()),
    path('dashmu', views.dash)
]