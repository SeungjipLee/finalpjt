from django.db import models

# Create your models here.
class Article1(models.Model):
    kor_co_nm = models.CharField(max_length=15)
    fin_prdt_nm = models.CharField(max_length=30)
    intr_rate_type = models.CharField(max_length=4)
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()


class Article2(models.Model):
    kor_co_nm = models.CharField(max_length=15)
    fin_prdt_nm = models.CharField(max_length=30)
    intr_rate_type = models.CharField(max_length=4)
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()


class Article3(models.Model):
    kor_co_nm = models.CharField(max_length=15)
    fin_prdt_nm = models.CharField(max_length=30)
    crdt_grad_avg = models.FloatField()