# Generated by Django 5.1.7 on 2025-03-30 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True)),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('past_surgeries', models.TextField(blank=True, null=True)),
                ('current_medications', models.TextField(blank=True, null=True)),
                ('primary_doctor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_doctor_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('medical_document', models.FileField(blank=True, null=True, upload_to='medical_documents/')),
                ('insurance_document', models.FileField(blank=True, null=True, upload_to='insurance_documents/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
