from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15, null=True)
    nama = models.CharField(max_length=50, null=True)
    program_studi = models.CharField(max_length=50, null=True)
    angkatan = models.CharField(max_length=20, null=True)
    alamat = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=40, null=True)

class SPP(models.Model):
    nama_spp = models.CharField(max_length=40, null=True)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    semester = models.CharField(max_length=20, null=True)
    tahun_akademik = models.CharField(max_length=20, null=True)
