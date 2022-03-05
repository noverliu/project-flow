import json
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from quickstart.flowableAPI import getDefinitions, startProcess
from quickstart.serializers import CommentSerializer, RequestLogSerializer, RequestSerializer, UserSerializer, GroupSerializer
from .models import Request, RequestLog

class UserViewSet(ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
  def me(self, request):
    serializer = UserSerializer(request.user, many = False, context={'request':request})
    return Response(serializer.data)

class GroupViewSet(ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [IsAuthenticated]

class RequestsViewSet(ModelViewSet):
  queryset = Request.objects.all()
  serializer_class = RequestSerializer
  permission_classes=[IsAuthenticated]

  @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
  def all(self, request):
    queryset = Request.objects.all()
    serializer = RequestSerializer(queryset, many = True, context={'request':request})
    return Response(serializer.data)

  def list(self, request):
    queryset = Request.objects.filter(createdBy=request.user)
    serializer = RequestSerializer(queryset, many = True, context={'request':request})
    return Response(serializer.data)
  
  @action(detail=False, methods=['get'])
  def get_by_instance(self, request):
    queryset = Request.objects.filter(processInstanceId=request.query_params.get('instanceId')).first()
    serializer=RequestSerializer(queryset, context={'request': request})
    return Response(serializer.data)

  @action(detail=True, methods=['get'])
  def logs(self, request, pk=None):
    logQuery=RequestLog.objects.filter(request=self.get_object())
    serializer=RequestLogSerializer(logQuery, many = True, context={'request':request})
    return Response(serializer.data)
    
  @action(detail=True, methods=['put'], name='Add comment')
  def add_comment(self, request, pk=None):
    reqObj=self.get_object()
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      reqObj.addComment(serializer.validated_data['message'], serializer.validated_data['operator'], request.user.username)
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def perform_create(self, serializer):
      serializer.save(createdBy=self.request.user)

  @action(detail=True, methods=['post'])
  def start_process(self, request, pk=None):
    reqObj = self.get_object()
    if reqObj.processInstanceId=='':
      definitions = getDefinitions(key='REVIEW-DEMO')
      definitionsId = definitions['data'][0]['id']
      res = startProcess(processId=definitionsId, requestId=reqObj.id, vars=json.loads(request.body.decode('utf-8')))
      reqObj.processInstanceId = res['id']
      reqObj.status='Process is running'
      reqObj.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response('Already has a process instance for this request.', status=status.HTTP_400_BAD_REQUEST)


  @action(detail=True, methods=["post"])
  def release(self, request, pk=None):
    reqObj = self.get_object()
    if reqObj.published!=True:
      reqObj.status='released'
      reqObj.processInstanceId=''
      reqObj.published=True
      reqObj.addComment('Release', 'flowable', request.user)
      reqObj.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response('This request was already published.', status=status.HTTP_400_BAD_REQUEST)
