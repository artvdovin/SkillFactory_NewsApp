from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post
from .filters import PostFilter

from .forms import PostForm
# Create your views here.

class News (ListView):
    model = Post
    ordering = '-date_add'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5


class PostNews (DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class Search (ListView):
    model = Post
    ordering = '-date_add'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostCreate_NW(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

class PostEdit_NW (UpdateView):
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class Delete_NW (DeleteView):
    model = Post
    template_name = 'news_del.html'
    success_url = reverse_lazy("news")


class PostCreate_AR(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

class PostEdit_AR (UpdateView):
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'


class Delete_AR (DeleteView):
    model = Post
    template_name = 'articles_del.html'
    success_url = reverse_lazy("news")