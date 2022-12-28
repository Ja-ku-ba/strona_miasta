from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post, Coment
from .forms import PostForm
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/forms/posts_list.html', context)

def post_add(request):
    form = PostForm()
    context = {'form':form}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title = request.POST.get('title'),
                body = request.POST.get('body'),
                owner = request.user
            )
            return redirect('posts_list')
        messages.info(request, 'Aby utworzyć nowy post musisz dodać tytuł, oraz treść')
        return redirect('post_add')
    return render(request, 'posts/forms/post_add.html', context)

def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        title_req = request.POST.get('title')
        body_req = request.POST.get('body')
        if title_req != "":
            post.title = title_req
        if body_req != "":
            post.req = body_req
        post.save()
        return redirect("posts_list")
    context = {'post':post}
    return render(request, 'posts/forms/post_edit.html', context)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'posts/forms/posts_delete.html', context)


