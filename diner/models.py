from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, default='김씨', unique=True)
    birth = models.CharField(max_length=100, null=True)
    level = models.CharField(max_length=100, null=True, default='사원')
    salary = models.PositiveBigIntegerField(null=False, default=0)
    memo = models.CharField(max_length=100, null=True)
