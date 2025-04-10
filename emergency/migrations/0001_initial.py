# Generated by Django 5.1.7 on 2025-03-31 07:35

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
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('primary_phone', models.CharField(max_length=15)),
                ('alternate_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('relation', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('husband', 'Husband'), ('wife', 'Wife'), ('son', 'Son'), ('daughter', 'Daughter'), ('brother', 'Brother'), ('sister', 'Sister'), ('grandfather', 'Grandfather'), ('grandmother', 'Grandmother'), ('uncle', 'Uncle'), ('aunt', 'Aunt'), ('guardian', 'Guardian'), ('friend', 'Friend'), ('colleague', 'Colleague'), ('neighbor', 'Neighbor'), ('other', 'Other')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
