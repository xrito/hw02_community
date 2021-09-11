from django.core.paginator import Paginator
from django.db.models import Count
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post, User


def index(request):
    post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, 10)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

    # posts = Post.objects.all()[:10]
    # context = {
    #     'posts': posts,
    # }
    # return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_list = group.posts.all()
    paginator = Paginator(group_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

    # group = get_object_or_404(Group, slug=slug)
    # posts = group.posts.all()[:10]
    # context = {
    #     'group': group,
    #     'posts': posts,
    # }
    # return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num_post = Post.objects.filter(author=user).count()
    context = {
        'user': user,
        'page_obj': page_obj,
        'num_post': num_post,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count = User.objects.filter().annotate(
        posts_count=Count('posts__author'))
    context = {
        'post': post,
        'count': count,
    }
    return render(request, 'posts/post_detail.html', context)
