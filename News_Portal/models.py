from django.db import models
from django.contrib.auth.models import User

# Класс написан
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

# Класс написан
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

# Готов класс
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    type = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()

# Класс написан
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Класс написан
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()
