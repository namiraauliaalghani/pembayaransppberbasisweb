from django.db import models

from PaymentGateway.models import Pembayaran
from pembayaranSPP.models import SPP, Mahasiswa


# Model Tagihan (Invoice)
class Tagihan(models.Model):
    id_mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    jumlah_tagihan = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status_tagihan = models.CharField(max_length=20, choices=[('LUNAS', 'Lunas'), ('BELUM', 'Belum Dibayar')], default='BELUM')
    tanggal_tagihan = models.DateField(auto_now_add=True)
    jatuh_tempo = models.DateField(null=True)


# Model Pengembalian Dana (Refund)
class PengembalianDana(models.Model):
    id_pembayaran = models.ForeignKey(Pembayaran, on_delete=models.CASCADE)
    tanggal_pengembalian = models.DateField(null=True)
    jumlah_dikembalikan = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    alasan_pengembalian = models.TextField(null=True)

