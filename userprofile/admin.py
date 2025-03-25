from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'date_of_birth', 'city', 'state', 'zip_code', 'created_at', 'updated_at')
    list_filter = ('gender', 'city', 'state')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'city', 'state')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("User Information", {
            "fields": ("user", "profile_picture", "gender", "date_of_birth"),
        }),
        ("Address Details", {
            "fields": ("address", "city", "state", "zip_code"),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)
