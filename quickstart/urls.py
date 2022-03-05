from rest_framework import routers
from quickstart import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('requests', views.RequestsViewSet)

urlpatterns = router.urls
