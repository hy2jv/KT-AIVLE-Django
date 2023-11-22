from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# 뷰객체: 서비스 처리 객체
def test1(request):
    return HttpResponse('blog/test1 응답')

def test2(request, no):
    print(type(no))
    return HttpResponse(no)

def list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/list.html', {'post_all':post_list})

def detail(request, no):
    post = get_object_or_404(Post, id=no)
    return render(request, 'blog/detail.html', {'post':post})