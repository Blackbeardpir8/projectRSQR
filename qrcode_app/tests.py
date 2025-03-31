from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from qrcode_app.models import QRCode

User = get_user_model()

class QRCodeAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="password123")
        self.client.login(email="test@example.com", password="password123")

    def test_generate_qr_code_view(self):
        response = self.client.get(reverse("qrcode_app:generate_qr"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your QR Code")
        self.assertTrue(QRCode.objects.filter(user=self.user).exists())

    def test_qr_code_model(self):
        qr_code = QRCode.objects.create(user=self.user)
        self.assertEqual(str(qr_code), f"QR Code for {self.user.email}")
