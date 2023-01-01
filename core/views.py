from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from posts.models import Post, Like, Dislike, Account, Coment
from posts.views import coment_add
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'core/home.html', context)

def search(request):    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    people = Account.objects.filter(
        Q(username__icontains=q)
    )
    posts = Post.objects.filter(
        Q(title__icontains=q) |
        Q(body__icontains=q)   
    )
    context = {'posts':posts, 'people':people, 'posts':posts}
    return render(request, 'core/search_results.html', context)

def post(request, pk):
    post_infos = Post.objects.get(id=pk)
    try:
        user_likes = Like.objects.get(post=post_infos, person=request.user)
    except:
        user_likes = None
    try:
        user_dislikes = Dislike.objects.get(post=post_infos, person=request.user)
    except:
        user_dislikes = None

    coments = Coment.objects.filter(comented_post=pk)
    context = {'post_infos':post_infos, 'user_likes':user_likes, 'user_dislikes':user_dislikes, 'coments':coments}
    add = coment_add(request, pk=pk)
    if add:
        return redirect('post', pk)

    return render(request, 'core/post.html', context)

def like_func(request, pk):
    post_req = Post.objects.get(id=pk)
    if request.method == "POST":
        #check if user aleready dilikes the post, then unduslike
        if Dislike.objects.filter(post=pk, person=request.user.id).exists() is True:
            dislike = Dislike.objects.get(post=pk, person=request.user.id)
            dislike.delete()
            post_req.save()
            post_req.reactions += 1
        #check if user already likes the post, then unlike
        if Like.objects.filter(post=pk, person=request.user.id).exists() is True:
            like = Like.objects.get(post=pk, person=request.user.id)
            like.delete()
            post_req.reactions -= 1
            post_req.save()
            return redirect('post', pk)
        #add like to post
        else:
            Like.objects.create(
                person = Account.objects.get(id=request.user.id),
                post = post_req
            )
            post_req.reactions += 1
            post_req.save()
            return redirect('post', pk)

def dislike_func(request, pk):
    post_req = Post.objects.get(id=pk)
    if request.method == "POST":
        #check if user aleready likes the post, then unlike
        if Like.objects.filter(post=pk, person=request.user.id).exists() is True:
            like = Like.objects.get(post=pk, person=request.user.id)
            like.delete()
            post_req.reactions -= 1
            post_req.save()
        #check if user already dislikes the post, then undislike
        if Dislike.objects.filter(post=pk, person=request.user.id).exists() is True:
            dislike = Dislike.objects.get(post=pk, person=request.user.id)
            dislike.delete()
            post_req.reactions += 1
            post_req.save()
            return redirect('post', pk)
        #add dislike to post
        else:
            Dislike.objects.create(
                person = Account.objects.get(id=request.user.id),
                post = post_req
            )
            post_req.reactions -= 1
            post_req.save()
            return redirect('post', pk)


def user_page(request, name):
    user_req = Account.objects.get(username = name)
    posts = Post.objects.filter(owner = user_req.id)
    context = {'user_req':user_req, 'posts':posts}

    return render(request, 'core/user_page.html', context)
























