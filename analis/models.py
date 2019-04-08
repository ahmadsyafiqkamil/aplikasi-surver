from django.db import models
from django.contrib.postgres.fields import JSONField
# from jsonfield import JSONField
# from analis.models import analis
# from django.contrib.auth.models import User


# Create your models here.
class proyek(models.Model):
    nama = models.CharField(max_length = 255, blank = True, verbose_name = "Nama Proyek")
    deskripsi = models.TextField(verbose_name = "Deskripsi Proyek");
    # id_user = models.ForeignKey(analis,on_delete = models.CASCADE)



class perangkat(models.Model):
    perangkat = JSONField()



class organisasi(models.Model):
    nama_organisasi = models.CharField(max_length = 255, blank = True)
    id_proyek = models.ForeignKey(proyek, on_delete=models.CASCADE)
