from django.db import models

# Create your models here.
# qraccess/models.py
from django.db import models
from users.models import CustomUser

class QRScanLog(models.Model):
    scanned_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scans_received')
    scanned_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='scans_done')
    ip_address = models.GenericIPAddressField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scan by {self.scanned_by} on {self.scanned_user} at {self.scanned_at}"
