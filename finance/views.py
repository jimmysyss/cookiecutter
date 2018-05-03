# Create your views here.
from django.http import HttpResponse
from finance.models import Currency


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
