from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Doctor, Schedule, Appointment

admin.site.site_header='Online Doctors Appointment'
admin.site.site_title='Administration'
admin.site.index_title='Online Doctors Appointment'

# Register your models here.
admin.site.unregister(Group)

@admin.register(Doctor)
class AdminDoctor(admin.ModelAdmin):
  list_display = ['dname', 'dmobile', 'qualification', 'specialist', 'yoe']


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
  list_display= ['doctors','days', 'time_slot']
  raw_id_fields = ["doctor"]

  def doctors(self, obj):
    return obj.doctor.dname
  
@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
  list_display= ['patients', 'doctors','appmadeon', 'appdate']
  # raw_id_fields = ["doctor"]

  def doctors(self, obj):
    return obj.doctor.dname
  
  def patients(self, obj):
    return obj.user.first_name+" "+obj.user.last_name
  
