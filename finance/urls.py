from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from finance.views import HelloWorldEntityViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'hello-world', HelloWorldEntityViewSet)


urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls)),
]
