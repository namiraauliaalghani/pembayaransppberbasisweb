from django.contrib import admin

# Register your models here.
from AcademicManagement.models import Fakultas, ProgramStudi
from BillingSystem.models import PengembalianDana, Tagihan
from PaymentGateway.models import Log_transaksi, Pembayaran
from pembayaranSPP.models import *

class FakultasAdmin(admin.ModelAdmin):
    list_display = ["nama_fakultas"]

class programstudiDdmin(admin.ModelAdmin):
    list_display = ["nama_program_studi"]
    #, "deskripsi"
class TagihanAdmin(admin.ModelAdmin):
    list_display = ["jumlah_tagihan","status_tagihan","jatuh_tempo"]

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ["program_studi", "alamat","nama","nim","email"]

class PembayaranAdmin(admin.ModelAdmin):
    list_display = ["tanggal_pembayaran", "metode_pembayaran","jumlah_bayar","status_pembayaran","id_mahasiswa"]


admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(SPP)
admin.site.register(Pembayaran, PembayaranAdmin)
admin.site.register(Log_transaksi)
admin.site.register(Fakultas, FakultasAdmin)
admin.site.register(ProgramStudi, programstudiDdmin)
admin.site.register(Tagihan,TagihanAdmin)
admin.site.register(PengembalianDana)
