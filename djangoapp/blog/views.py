from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404

# query-set = more than one object 

PER_PAGE = 9

## the 'manager' works on the database. In this case, the 'objects'

def index(request): # this one below
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Home - '
        }
    )


def page(request, slug):
    page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()
    
    if page_obj is None:
        raise Http404()
    page_title = f'{page_obj.title} - Page - '
    
    
    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_obj,
            'page_title': page_title,
        }
    )


def post(request, slug):
    post_obj = Post.objects.get_published().filter(slug=slug).first()
    
    if post_obj is None:
        raise Http404()
    
    page_title = f'{post_obj.title} - Post - '
    
    return render(
        request,
        'blog/pages/post.html',
        {
            'post':post_obj,
            'page_title': page_title,

        }
    )

def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()

    if user is None:
        raise Http404()

    posts = Post.objects.get_published().filter(created_by__pk=author_pk)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    user_fullname = user.username 

    if user.first_name:
        user_fullname = f'{user.first_name} {user.last_name}'
    page_title = f'{user_fullname} posts - '


    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )

def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(posts) == 0:
        raise Http404()
    page_title = f'{page_obj[0].category.name} - Category - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )

def tags(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(posts) == 0:
        raise Http404()
    page_title = f'{page_obj[0].tags.first().name} - Tag - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )

def search(request): # The one with capital letter is a HTTP method, and the another one is from python 
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value) 
    )[:PER_PAGE]

    page_title = f'{search_value[:30]} - Search - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': page_title,
        }
    )