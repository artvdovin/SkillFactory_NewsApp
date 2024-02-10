from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Author (models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username

    def update_rating(self):
        rt= 0
        for el in self.post_set.all():
            rt +=el.rating
        rt = rt*3
        for el in self.author.comment_set.all():
            rt +=el.rating
        for el in Comment.objects.filter(commentPost__author=self):
            rt +=el.rating
        print (rt)
        self.rating=rt
        self.save()

class Category (models.Model):
    name = models.CharField (max_length=10, unique=True)

    def __str__(self):
        return self.name


class Post (models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date_add = models.DateTimeField (auto_now_add=True)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_TYPE = (
        (NEWS , "Новость"),
        (ARTICLE, "Статья")
    )
    categoryType = models.CharField (max_length=2,choices=CATEGORY_TYPE)
    postCategory = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField (max_length=100)
    post = models.TextField()
    rating = models.IntegerField (default=0)
    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.post[0:123]+'...'

    def get_absolute_url(self):
        return reverse('new', args=[str(self.id)])

class PostCategory (models.Model):
    postThround = models.ForeignKey (Post,on_delete=models.CASCADE)
    categoryThround = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment (models.Model):
    commentPost = models.ForeignKey (Post,on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    commentDate = models.DateTimeField (auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()