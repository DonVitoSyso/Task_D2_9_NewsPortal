from django.db import models


class Author(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

# Готов класс
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    type = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    category = models.ManyToManyField(Category, throught='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    pass
