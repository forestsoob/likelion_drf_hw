from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200) # 가수 설명
    debut = models.DateField() # 데뷔일자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs') # 해당 노래 부른 사람
    release =  models.DateField()  # 출시일
    content = models.TextField(max_length=200) # 노래 설명
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
