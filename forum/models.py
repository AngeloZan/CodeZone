from django.db import models
from django.conf import settings

class ForumPost(models.Model):
    title                       = models.CharField(max_length=60, blank=False, null=False)
    text                        = models.TextField(max_length=10000, blank=False, null=False)
    author                      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_published              = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    date_updated                = models.DateTimeField(auto_now=True, verbose_name='date updated')

    def __str__(self):
        return self.title


