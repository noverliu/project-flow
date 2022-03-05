from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
from .models import Request, RequestLog, UserExtensions
from rest_framework import serializers

class UserExSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = UserExtensions
    fields = ["flowableKey"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
  extensions = UserExSerializer(many=False)
  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'email', 'groups', 'extensions']
  def create(self, validated_data):
    extensions = validated_data.pop('extensions')
    user = User.objects.creat(**validated_data)
    UserExtensions.objects.create(user=user, **extensions)
  def update(self, instance, validated_data):
    extensions = validated_data.pop('extensions')
    UserExtensions.objects.filter(user=instance).delete()
    UserExtensions.objects.create(user=instance, **extensions)
    instance.save()
    return instance
  
class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class RequestLogSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = RequestLog
    fields = ['uid', 'request', 'message','operator', 'created', 'createdBy']

class RequestSerializer(serializers.HyperlinkedModelSerializer):
  logs = RequestLogSerializer(many=True, read_only=True)
  class Meta:
    model = Request
    fields = ['id','project', 'data', 'status', 'comments', 'processInstanceId', 'published', 'created', 'createdBy', 'logs']

class CommentSerializer(serializers.Serializer):
  message = serializers.CharField(max_length=5000)
  operator = serializers.CharField(max_length=150)


  