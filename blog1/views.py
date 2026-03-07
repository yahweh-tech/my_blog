from django.shortcuts import render
from .models import Blog


def index(request):
    Blogs=Blog.objects.all()
    return render(request,"index.html",{'Blogs':Blogs})

def blogs(request,pk):
    Blogs=Blog.objects.get(id=pk)
    return render(request,"view_blog.html",{'Blogs':Blogs})