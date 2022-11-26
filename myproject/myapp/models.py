from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # class Gender(models.TextChoices):
    #     Male='Male'
    #     Female='Female'
    mobile=models.CharField(max_length=12, verbose_name='Contact Number')
    age=models.CharField(max_length=2)
    gender=models.CharField(max_length=6)

class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=255, verbose_name='Doctor Name')
    dmobile=models.CharField(max_length=15, verbose_name='Doctor Contact Number')
    qualification=models.CharField(max_length=255)
    specialist=models.CharField(max_length=255)
    yoe=models.CharField(max_length=2, verbose_name='Year of Experience')

class Schedule(models.Model):
    sid=models.AutoField(primary_key=True)
    days=models.CharField(max_length=255, verbose_name='Doctors Availble')
    time_slot=models.CharField(max_length=255, verbose_name='Timing')
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor', verbose_name='Doctor')

class Appointment(models.Model):
    apid=models.AutoField(primary_key=True)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors', verbose_name='Doctors')
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient', verbose_name='Patient')
    appmadeon=models.DateField(auto_now_add=True, blank=False, verbose_name='Appointment Made Date')
    appdate=models.DateField(verbose_name='Appointment Date')
