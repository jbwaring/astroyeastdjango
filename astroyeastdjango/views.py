from django.http import HttpResponse
from . import hardware

def index(request):
    hardware.RGB_test()
    return HttpResponse("Hello, world. You're at the polls index.")