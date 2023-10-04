from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post

# Create your views here.

PER_PAGE = 9

## the 'manager' works on the database. In this case, the 'objects'

def index(request): # this one below
    posts = Post.objects.get_published
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


def page(request):
    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request, slug):
    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )