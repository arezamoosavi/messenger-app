from django.urls import path
from . import views

app_name = 'chat_service'

urlpatterns = [
    path('',views.TranslatetoMorse.as_view(),name='translate'),
]