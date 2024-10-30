from django.db import models

from pembayaranSPP.models import SPP, Mahasiswa

# Create your models here.
class Pembayaran(models.Model):
    tanggal_pembayaran =  models.DateField(null=True)
    metode_pembayaran =  models.CharField(max_length=20, null=True)
    jumlah_bayar =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status_pembayaran = models.CharField(max_length=20, null=True)
    id_mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    id_spp = models.ForeignKey(SPP, on_delete=models.CASCADE)

class Log_transaksi(models.Model):
    id_pembayaran = models.ForeignKey(Pembayaran, on_delete=models.CASCADE)
    waktu_log = models.DateField(null=True)
    status_transaksi =  models.CharField(max_length=20, null=True)