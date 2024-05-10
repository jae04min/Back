from django.db import models

from rest_framework import serializers

class Hospital(models.Model):
    longitude = models.FloatField(null=False, default="Comment")  # 경도
    latitude = models.FloatField(null=False, default="Comment")  # 위도
    place_name = models.CharField(max_length=30, null=False, default="Comment")  # 장소이름
    category = models.CharField(max_length=10, null=False, default="Comment")  # 카테고리
    address = models.CharField(max_length=30, null=False, default="Comment")  # 주소

    class Meta:
        db_table = 'map'  # 테이블 이름을 'map'으로 설정

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
