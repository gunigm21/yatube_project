from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
import datetime

def index(request):
    '''
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 
    '''
    '''
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    
    author = User.objects.get(username="leo")
    keyword = "утро"
    posts = Post.objects.filter(
        pub_date__range=(start_date, end_date), 
        text__contains=keyword, 
        author=author
        )
    return render(request, 'posts/index.html', {'posts': posts})
    '''
    author = User.objects.get(username="leo")
    keyword = request.GET.get("q", None)
    if keyword:
        posts = Post.objects.filter(
            text__contains=keyword, 
            author=author
            ).select_related('author', 'group').all()
    else:
        posts = None

    return render(request, 'posts/index.html', {'posts': posts, 'keyword': keyword})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 

