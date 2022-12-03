from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    content_text = models.TextField(null=True, blank=True)
    ctime = models.DateTimeField(null=True)
    utime = models.DateTimeField(null=True)
    def __str__(self):
        return self.title