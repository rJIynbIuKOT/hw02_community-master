from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Group


def index(request):
    # latest = Post.objects.order_by("-pub_date")[:11]
    # return render(request, "index.html", {"posts": latest})
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 10)  # По 10 статьи на каждой странице.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page': page, 'posts': posts})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})