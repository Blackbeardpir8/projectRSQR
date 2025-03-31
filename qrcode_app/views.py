from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from io import BytesIO
import qrcode

@login_required
def generate_qr_code(request):
    user = request.user  # Get the currently logged-in user

    # Check if the QR code already exists
    if user.qr_code and user.qr_code.qr_image:
        return render(request, "qrcode_app/qr_code.html", {"qr_instance": user.qr_code})

    # Generate the URL dynamically
    profile_url = request.build_absolute_uri(f"/profile/{user.id}/")

    # Generate QR Code
    qr = qrcode.make(profile_url)
    qr_io = BytesIO()
    qr.save(qr_io, format="PNG")

    # Save the QR code to the user's profile
    user.qr_code.qr_image.save(f"user_{user.id}_qr.png", ContentFile(qr_io.getvalue()), save=True)

    return render(request, "qrcode_app/qr_code.html", {"qr_instance": user.qr_code})
