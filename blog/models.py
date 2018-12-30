from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# class is like table
class Post(models.Model):
    # field is like column
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse method returns full path as a string
        return reverse('post-detail', kwargs={'pk':self.pk})
