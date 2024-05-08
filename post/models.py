from django.db import models
from django.db.models import Model

# Create your models here.
class PostModel(models.Model):
    content_id = models.BigAutoField(primary_key=True, null=False,editable=True)
    content_title = models.CharField(max_length=30)
    content = models.CharField(max_length=300, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    likes = models.SmallIntegerField(null=True, max_length=10)  
    image = models.ImageField(default=None)