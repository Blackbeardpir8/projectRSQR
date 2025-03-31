from django.db import models
from users.models import CustomUser

class EmergencyContact(models.Model):
    RELATIONSHIP_CHOICES = [
    ('father', 'Father'),
    ('mother', 'Mother'),
    ('husband', 'Husband'),
    ('wife', 'Wife'),
    ('son', 'Son'),
    ('daughter', 'Daughter'),
    ('brother', 'Brother'),
    ('sister', 'Sister'),
    ('grandfather', 'Grandfather'),
    ('grandmother', 'Grandmother'),
    ('uncle', 'Uncle'),
    ('aunt', 'Aunt'),
    ('guardian', 'Guardian'),
    ('friend', 'Friend'),
    ('colleague', 'Colleague'),
    ('neighbor', 'Neighbor'),
    ('other', 'Other'),
]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="emergency_contacts")
    name = models.CharField(max_length=255)
    primary_phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    relation = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_relation_display()})"
