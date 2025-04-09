from django.shortcuts import render, get_object_or_404
from users.models import CustomUser
from emergency.models import EmergencyContact
from userprofile.models import UserProfile
from medical.models import MedicalDetail
from .models import QRScanLog
from .utils import get_client_ip

def qr_profile_view(request, user_id):
    scanned_user = get_object_or_404(CustomUser, id=user_id)

    emergency_contacts = EmergencyContact.objects.filter(user=scanned_user)
    profile = UserProfile.objects.filter(user=scanned_user).first()
    medical = MedicalDetail.objects.filter(user=scanned_user).first()
    scanned_by = request.user if request.user.is_authenticated else None
    ip_address = get_client_ip(request)

    QRScanLog.objects.create(
        scanned_user=scanned_user,
        scanned_by=scanned_by,
        ip_address=ip_address
    )

    show_sensitive_data = (
        request.user.is_authenticated and (
            request.user == scanned_user or request.user.role in ["doctor", "admin"]
        )
    )

    return render(request, "qr/scan_result.html", context={
    "scanned_user": scanned_user,
    "profile": profile,
    "emergency_contacts": emergency_contacts,
    "medical": medical if show_sensitive_data else None,
    "show_sensitive_data": show_sensitive_data,
})
