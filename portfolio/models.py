# models.py
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200)  # 예: "2025년 최고의 영화"
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    topic = models.ForeignKey(Topic, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='items/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    item = models.ForeignKey(Item, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()  # 1~5점
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('item', 'user')  # 중복 투표 방지
