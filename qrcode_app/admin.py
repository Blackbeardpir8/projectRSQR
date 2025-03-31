from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'qr_image')
    search_fields = ('user__email',)
