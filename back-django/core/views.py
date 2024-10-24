from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

def blog_view(request) -> HttpResponse:
    posts: BaseManager[Post] = Post.objects.all()
    tags = Tag.objects.all()
    print(tags)

    # Verificar se uma tag foi selecionada
    selected_tag = request.GET.get('tag')
    if selected_tag:
        posts = posts.filter(tags__name=selected_tag)

    # Verificar se há uma pesquisa
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(title__icontains=search_query)

    # Configurar paginação com 5 itens por página
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'core/blog.html', {
        'posts': paginated_posts,
        'tags': tags
    })

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'core/post_detail.html', {'post': post})
