from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def blog_index(request):
    projects= Post.objects.all().order_by('-created_on')
    context={
        'posts': posts,
    }
    return render(request,'blog_index.html',context )

def blog_detail(request,pk):
    project = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'project_detail.html', context)
