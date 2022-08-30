
from djangp.http import httpresponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("CSDN读者你好啊")

def login(request):
    return redirect("/index")
