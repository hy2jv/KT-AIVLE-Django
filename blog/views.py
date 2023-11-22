from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

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
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post':post, 
                                                'comment_all':comment_list, 
                                                'tag_list':tag_list,})

def profile(request):
    user = User.objects.first()
    return render(request, 'blog/profile.html', {'user':user})

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})

def test3(request):
    return render(request, 'blog/form_test.html')