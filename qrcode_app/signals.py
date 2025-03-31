from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from users.models import CustomUser
from qrcode_app.models import QRCode

@receiver(post_save, sender=CustomUser)
def create_qr_code(sender, instance, created, **kwargs):
    if created:
        QRCode.objects.create(user=instance)

@receiver(post_delete, sender=QRCode)
def delete_qr_image(sender, instance, **kwargs):
    if instance.qr_image:
        instance.qr_image.delete(save=False)
