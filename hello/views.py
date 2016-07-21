from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from hello.models import Post

# Create your views here.


def hello(request):
    # return HttpResponse('Hello world!')
    now = datetime.now()
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
    # raise RuntimeError
