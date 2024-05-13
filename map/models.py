from django.db import models

class Hospital(models.Model):
    longitude = models.FloatField(null=False, default="Comment")  # 경도
    latitude = models.FloatField(null=False, default="Comment")  # 위도
    place_name = models.CharField(max_length=30, null=False, default="Comment")  # 장소이름
    category = models.CharField(max_length=10, null=False, default="Comment")  # 카테고리
    address = models.CharField(max_length=30, null=False, default="Comment")  # 주소

    class Meta:
        db_table = 'map'  # 테이블 이름을 'map'으로 설정