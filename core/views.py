from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages


from posts.models import Post, Like, Dislike, Account, Coment, Interractions
from posts.views import coment_add, coment_delete, post_delete
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'core/home.html', context)

def search(request):    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q == '':
        messages.info(request, 'Wprowadzono puste zapytanie.')
        return redirect('home')
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
            check_interactions(request.user, post_req, False)
        #check if user already likes the post, then unlike
        if Like.objects.filter(post=pk, person=request.user.id).exists() is True:
            like = Like.objects.get(post=pk, person=request.user.id)
            like.delete()
            post_req.reactions -= 1
            post_req.save()
            check_interactions(request.user, post_req, False)
            return redirect('post', pk)
        #add like to post
        else:
            Like.objects.create(
                person = Account.objects.get(id=request.user.id),
                post = post_req
            )
            post_req.reactions += 1
            post_req.save()
            check_interactions(request.user, post_req, True)
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
            check_interactions(request.user, post_req, False)
        #check if user already dislikes the post, then undislike
        if Dislike.objects.filter(post=pk, person=request.user.id).exists() is True:
            dislike = Dislike.objects.get(post=pk, person=request.user.id)
            dislike.delete()
            post_req.reactions += 1
            post_req.save()
            check_interactions(request.user, post_req, False)
            return redirect('post', pk)
        #add dislike to post
        else:
            Dislike.objects.create(
                person = Account.objects.get(id=request.user.id),
                post = post_req
            )
            post_req.reactions -= 1
            post_req.save()
            check_interactions(request.user, post_req, True)
            return redirect('post', pk)


def user_page(request, name):
    user_req = Account.objects.get(username = name)
    posts = Post.objects.filter(owner = user_req.id)
    context = {'user_req':user_req, 'posts':posts}

    return render(request, 'core/user_page.html', context)

def check_interactions(user, post_id, status):                                                      #when you add deltee coment function, change it to check 
    coment_status = False                                                                           #coment exist, then change interaction status
    try:
        coment = Coment.objects.get(comented_post=post_id, owner=user)
        coment_status = True
    except:
        pass    
    if status is False:
        iter = Interractions.objects.get(person=user, post=post_id)
        iter.delete()
        return True
    Interractions.objects.create(
        person = user,
        post = post_id
    )
    return True

def user_interactions(request, username):
    user_req = Account.objects.get(username=username)
    likes = Like.objects.filter(person = user_req.id)
    dislikes = Dislike.objects.filter(person = user_req.id)
    coments = Coment.objects.filter(owner = user_req.id)
    posts = likes | dislikes | coments
    context = {'user_req':user_req, 'posts':posts}
    return render(request, 'core/user_post_interactions.html', context)






















