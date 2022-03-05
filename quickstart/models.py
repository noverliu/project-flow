from email import message
from email.policy import default
from operator import truediv
from django.db import models
from django.contrib.auth.models import User

class UserExtensions(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='extensions')
  flowableKey=models.CharField(max_length=200, blank=True, null=True)

# Create your models here.
class Request(models.Model):
  id = models.AutoField(primary_key=True)
  project = models.CharField(max_length=200, blank=True)
  data = models.JSONField(blank=True, null=True)
  status = models.CharField(max_length=100, default='Not start yet')
  assignee = models.CharField(max_length=200, blank=True)
  comments = models.CharField(max_length=2000, blank=True, null=True)
  processInstanceId = models.CharField(max_length=50, blank=True)
  published=models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  def addComment(self, msg, operator, createdBy):
    RequestLog.objects.create(request=self, message=msg, operator=operator, createdBy=createdBy)

class RequestLog(models.Model):
  uid = models.AutoField(primary_key=True)
  request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='logs', related_query_name='log')
  operator = models.CharField(max_length=200, default='sys')
  created = models.DateTimeField(auto_now_add=True)
  message = models.CharField(max_length=5000, blank=True, null=True)
  createdBy = models.CharField(max_length=150, blank=True, null=True)