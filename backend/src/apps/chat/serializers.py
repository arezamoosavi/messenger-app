from core.models import User
from rest_framework import serializers
from apps.chat.models import Message


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'online']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
