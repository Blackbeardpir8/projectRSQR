from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile
from django.urls import reverse
import qrcode
from io import BytesIO

class QRCode(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="qr_code")
    qr_image = models.ImageField(upload_to="qr_codes/", blank=True, null=True)

    def save(self, *args, **kwargs):
        """Generate and save a dynamic QR code for the user's profile."""
        if not self.pk or not self.qr_image:  # Generate QR only if it doesn't exist
            profile_url = reverse("users:profile", kwargs={"user_id": self.user.id})
            full_url = f"http://127.0.0.1:8000{profile_url}"

            qr = qrcode.make(full_url)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            self.qr_image.save(f"qr_{self.user.id}.png", ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"QR Code for {self.user.email}"
