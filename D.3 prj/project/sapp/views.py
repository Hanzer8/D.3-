from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostsList(ListView):
   model = Post
   ordering = 'post_autor'
   template_name = 'sapp/posts.html'
   context_object_name = 'posts'


class PostDetail(DetailView):
   model = Post
   template_name = 'sapp/post.html'
   context_object_name = 'post'

   def get_context_data(self, **kwargs):
      # С помощью super() мы обращаемся к родительским классам
      # и вызываем у них метод get_context_data с теми же аргументами,
      # что и были переданы нам.
      # В ответе мы должны получить словарь.
      context = super().get_context_data(**kwargs)
      # К словарю добавим текущую дату в ключ 'time_now'.
      context['time_now'] = datetime.utcnow()
      # Добавим ещё одну пустую переменную,
      # чтобы на её примере рассмотреть работу ещё одного фильтра.
      # context['next_sale'] = None
      return context