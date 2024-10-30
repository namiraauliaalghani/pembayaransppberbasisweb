from django.db import models

# Create your models here.
# Model Mahasiswa dan Admin sudah ada di pembayaranSPP

# Model Fakultas
class Fakultas(models.Model):
    nama_fakultas = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return str(self.nama_fakultas)

# Model Program Studi
class ProgramStudi(models.Model):
    nama_program_studi = models.CharField(max_length=100)
    fakultas = models.ForeignKey(Fakultas, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.nama_program_studi)





