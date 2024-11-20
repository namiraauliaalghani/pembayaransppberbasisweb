from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from AcademicManagement.models import Fakultas, ProgramStudi
from BillingSystem.models import PengembalianDana, Tagihan
from PaymentGateway.models import Log_transaksi, Pembayaran
from pembayaranSPP.models import *

@admin.register(Fakultas)
class FakultasAdmin(admin.ModelAdmin):
    list_display = ["nama_fakultas"]

@admin.register(ProgramStudi)
class programstudiDdmin(admin.ModelAdmin):
    list_display = ["nama_program_studi"]
    #, "deskripsi"
@admin.register(Tagihan)
class TagihanAdmin(admin.ModelAdmin):
    list_display = ["jumlah_tagihan","status_tagihan","jatuh_tempo"]

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ["program_studi", "alamat","nama","nim","email"]

@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    list_display = ["tanggal_pembayaran", "metode_pembayaran","jumlah_bayar","status_pembayaran","id_mahasiswa"]

    
@admin.register(SPP)
class SPPAdmin(admin.ModelAdmin):
    pass

@admin.register(PengembalianDana)
class PengembalianDana(admin.ModelAdmin):
    pass

@admin.register(Log_transaksi)
class Log_transaksi(admin.ModelAdmin):
    pass 



