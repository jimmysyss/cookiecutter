# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from finance.models import Currency, HelloWorldEntity
from finance.serializer import HelloWorldEntitySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class HelloWorldEntityViewSet(viewsets.ModelViewSet):
    queryset = HelloWorldEntity.objects.all()
    serializer_class = HelloWorldEntitySerializer
