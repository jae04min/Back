from django.db import models

class Pet(models.Model):
    SEX_CHOICES = [
        (0, '수컷'),
        (1, '암컷')
    ]

    PET_TYPE_CHOICES = [
        ('D', '강아지'),
        ('C', '고양이'),
        ('O', '기타')
    ]
    
    pet_id = models.BigAutoField(primary_key=True, null=False, editable=True)
    pet_name = models.CharField(max_length=30, null=False)
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES, default='강아지')
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, default=0)
    img = models.ImageField(upload_to='pet_images/')  # 이미지를 저장할 경로 설정

    class Meta:
        db_table = 'mypage'