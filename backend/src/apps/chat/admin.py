from django.contrib import admin
from apps.chat.models import Message, UserProfile

# Register your models here.
admin.site.register(Message)
admin.site.register(UserProfile)
