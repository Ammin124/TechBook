from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

class Post(models.Model):
    title = models.CharField(max_length=150)
    titleTag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='post')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, related_name='blogPosts')

    def totalLikes(self):
        return self.liked.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def textFild(self):
        return self.body[:300] + '... ... ... !'

    class Meta:
        ordering = ['-modified']

    def get_absolute_url(self):
        return reverse('index')


class About(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    studentID = models.IntegerField()
    img = models.ImageField(upload_to='about')
    linkedIn = models.URLField(max_length=500, blank=True)
    facebook = models.URLField(max_length=500, blank=True)
    instagram = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    date= models.DateTimeField(default= now)

    def __str__(self):
        return self.user.username + ": " + self.comment[0:20]


