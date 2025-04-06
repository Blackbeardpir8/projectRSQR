from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from io import BytesIO
import qrcode
from .models import QRCode
from django.urls import reverse

@login_required
def generate_qr_code(request):
    user = request.user

    # ✅ Always ensure a QRCode object exists
    qr_instance, created = QRCode.objects.get_or_create(user=user)

    # If QR image already exists, just show it
    if qr_instance.qr_image:
        return render(request, "qrcode_app/qr_code.html", {"qr_instance": qr_instance})

    # Generate profile URL
    profile_url = request.build_absolute_uri(reverse("user-profile")) 


    # Generate QR Code
    qr = qrcode.make(profile_url)
    qr_io = BytesIO()
    qr.save(qr_io, format="PNG")

    # Save QR image to the model
    qr_instance.qr_image.save(f"user_{user.id}_qr.png", ContentFile(qr_io.getvalue()), save=True)

    return render(request, "qrcode_app/qr_code.html", {"qr_instance": qr_instance})
