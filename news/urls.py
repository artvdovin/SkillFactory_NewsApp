from django.urls import path
# Импортируем созданное нами представление
from .views import News,PostNews, Search, PostCreate_NW, PostEdit_NW, Delete_NW, PostEdit_AR, PostCreate_AR,Delete_AR, subscriptions

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', News.as_view(), name='news'),
   path('<int:pk>', PostNews.as_view(), name="new"),
   path('search/', Search.as_view(),name='search'),
   path('news/create/', PostCreate_NW.as_view(), name='create_nw'),
   path('news/<int:pk>/edit', PostEdit_NW.as_view(), name="news_edit"),
   path('news/<int:pk>/delete', Delete_NW.as_view(), name="news_delete"),
   path('articles/create/', PostCreate_AR.as_view(), name='create_ar'),
   path('articles/<int:pk>/edit', PostEdit_AR.as_view(), name="articles_edit"),
   path('articles/<int:pk>/delete', Delete_AR.as_view(), name="articles_delete"),
   path('subscriptions/', subscriptions, name='subscriptions'),


]