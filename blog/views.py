from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# 뷰객체: 서비스 처리 객체
def test1(request):
    return HttpResponse('blog/test1 응답')

def test2(request, no):
    print(type(no))
    return HttpResponse(no)

def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get('keyword')
    if search_key:
        post_list = Post.objects.filter(title__contains=search_key)
    return render(request, 'blog/list.html', {'post_all':post_list, 'q':search_key})

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
    print('요청 방식:', request.method)
    print('Get방식으로 전달된 문자열:', request.GET)
    print('Post방식으로 전달된 문자열:', request.POST)
    
    return render(request, 'blog/form_test.html')

#Form 기반 Data 추가
def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print('cleaned_data:', form.cleaned_data)
            # DB에 추가
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostModelForm()
    return render(request, 'blog/post_form.html', {'form':form})

# Form 기반 Data 수정
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_update.html', {'form':form})

# Data 삭제
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post':post})