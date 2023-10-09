from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q
# Create your views here.

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
        }
    )


def page(request, slug):
    page = Page.objects.get_published().filter(slug=slug).first()
    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
        }
    )


def post(request, slug):
    post = Post.objects.get_published().filter(slug=slug).first()
    return render(
        request,
        'blog/pages/post.html',
        {
            'post':post
        }
    )

def created_by(request, author_pk):
    posts = Post.objects.get_published().filter(created_by__pk=author_pk)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def tags(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def search(request): # The one with capital letter is a HTTP method, and the another one is from python 
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value) 
    )[:PER_PAGE]

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value
        }
    )