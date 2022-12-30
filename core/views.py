from django.shortcuts import render

from posts.models import Post
# Create your views here.

def home(request):

    # feed panel
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'core/home.html', context)



