from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from core.models import User
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from apps.chat.models import Message, UserProfile
from apps.chat.serializers import MessageSerializer, UserSerializer

@csrf_exempt
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.create_user(email=data['email'], password=data['password'])
            UserProfile.objects.create(user=user)
            return Response(data, status=201)
        except Exception:
            return Response({'error': "Something went wrong"}, status=400)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return Response({'error': "Something went wrong"}, status=400)
    if request.method == "GET":
        data = {'users': User.objects.exclude(email=request.user.email),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}
        return Response(data, status=200)
                      
