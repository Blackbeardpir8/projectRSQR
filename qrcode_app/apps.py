from django.apps import AppConfig

class QrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "qrcode_app"

    def ready(self):
        import qrcode_app.signals  # Ensure signals are connected
