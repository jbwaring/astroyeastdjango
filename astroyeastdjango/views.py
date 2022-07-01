from django.http import HttpResponse
from hardware import RGB_test

def index(request):
    RGB_test()
    return HttpResponse("Hello, world. You're at the polls index.")