from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    excerpt = models.TextField(null=True)
    content = models.TextField(blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    class Meta:
        ordering = ('-published',)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title + ' | ' + str(self.name)

    class Meta:
        ordering = ('published',)



