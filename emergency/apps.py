from django.apps import AppConfig

class EmergencyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emergency"

    def ready(self):
        import emergency.templatetags.custom_tags  # Ensure tags are imported
