from django.db import models
from django.db.models import Model
from back import settings


# Create your models here.
class PostModel(models.Model):
    content_id = models.BigAutoField(primary_key=True, null=False,editable=True)
    content_title = models.CharField(max_length=30)
    content = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.SmallIntegerField(default=0)
    image = models.ImageField(default=None)
    type = models.CharField(max_length=10, null=False, editable=False, default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)
    