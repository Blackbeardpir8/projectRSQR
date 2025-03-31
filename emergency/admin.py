from django.contrib import admin
from .models import EmergencyContact

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "primary_phone", "relation")  # Columns in admin list view
    search_fields = ("name", "primary_phone", "relation")  # Enable search by name, phone, relation
    list_filter = ("relation",)  # Add a filter for relation type
    ordering = ("name",)  # Order contacts alphabetically by name
    readonly_fields = ("user",)  # Prevent modifying the user field in admin
