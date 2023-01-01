from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post, Coment, get_image_filepath
from .forms import PostForm, ComentForm
from users.models import Account
# Create your views here.

def post_coment(request):
    return render(request, 'posts/post_coment.html')


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/forms/posts_list.html', context)

def post_add(request):
    form = PostForm()
    context = {'form':form}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post.objects.create(
                title = request.POST.get('title'),
                body = request.POST.get('body'),
                owner = request.user,
            )
            new_post.image = request.FILES.get('image')
            new_post.save()
            return redirect('post', new_post.id)
        messages.info(request, 'Aby utworzyć nowy post musisz dodać tytuł, oraz treść')
        return redirect('home')
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

def post_delete(request, pk, user_req):
    post = Post.objects.get(id=pk)
    user = Account.objects.get(username=user_req)
    if post.owner == user:
        if request.method == 'POST':
            post.delete()
            return redirect('home')
    messages.error(request, 'Nie masz uprawnień do wykonania tej akcji')
    return redirect('home')

def coment_list(request):
    coments = Coment.objects.all()
    context = {'coments':coments}
    return render(request, 'posts/forms/coment_list.html', context)

def coment_add(request, pk):
    form = ComentForm()
    comented_post_request = Post.objects.get(id=pk)
    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            Coment.objects.create(
                owner = request.user,
                comented_post = comented_post_request,
                body = request.POST.get('body')
            )
            return True

def coment_delete(request, pk, user_req):
    coment = Coment.objects.get(id=pk)
    user = Account.objects.get(username=user_req)
    if coment.owner == user:
        if request.method == 'POST':
            coment.delete()
            return redirect('post', coment.comented_post.id)
    messages.error(request, 'Nie masz uprawnień do wykonania tej akcji')
    return redirect('post', coment.comented_post.id)