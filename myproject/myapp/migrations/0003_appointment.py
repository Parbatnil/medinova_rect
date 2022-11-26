# Generated by Django 3.2.15 on 2022-10-31 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('apid', models.AutoField(primary_key=True, serialize=False)),
                ('appmadeon', models.DateField(auto_now_add=True, verbose_name='Appointment Made Date')),
                ('appdate', models.DateField(verbose_name='Appointment Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='myapp.doctor', verbose_name='Doctors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL, verbose_name='Patient')),
            ],
        ),
    ]
