from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import datetime
from . models import Schedule, Doctor, Appointment

from  . forms import MyRegForm, MyLoginFrm, ChangeProfileFrm, AppointmentForm
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    else:
        return render(request, 'myapp/index.html')
    

def about(request):
    return render(request, 'myapp/about.html')

def userReg(request):
    if request.POST:
        form=MyRegForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Patient registration is successful')
            except Exception as e:
                messages.error(request, 'Patient registration is unsuccessful')
    else:
        form=MyRegForm()
    context={'form':form}
    return render(request, 'myapp/reg.html', context);

def userLog(request):
    if request.POST:
        form=MyLoginFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile')
    else:
        form=MyLoginFrm()
    return render(request, 'myapp/login.html', {'form':form});

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def profile(request):
    if request.user.is_authenticated:
        alldoc=Schedule.objects.raw("SELECT s.*, d.* FROM myapp_schedule s INNER JOIN myapp_doctor d ON s.doctor_id=d.did")
        return render(request, 'myapp/profile.html', {'alldoc':alldoc})
    else:
        return HttpResponseRedirect('/login')

def makeAppoint(request,did):
    if request.user.is_authenticated:
        if request.POST:
            schedule=Schedule.objects.get(doctor=did)
            sDays=schedule.days.split()
            appdate=datetime.datetime.strptime(request.POST.get('appdate'), "%Y-%m-%d").date()
            appSDay=appdate.strftime('%A')
            # print(appSDay)
            # print(sDays)
            form=AppointmentForm(request.POST)
            if form.is_valid():
                f=0
                for d in sDays:
                    if appSDay==d:
                        f=1
                if f==1:
                    instance=form.save(False)
                    instance.doctor_id = did
                    instance.user_id=request.user.id
                    instance.save()
                    messages.success(request, 'Your appointment has been made successfully')
                else:
                    messages.error(request, 'Doctor will not available that day')
        else:
            form=AppointmentForm()
        alldoc=Schedule.objects.raw("SELECT s.*, d.* FROM myapp_schedule s INNER JOIN myapp_doctor d ON s.doctor_id=d.did WHERE s.doctor_id={}".format(did) )
        return render(request, 'myapp/appointment.html',{'alldoc':alldoc, 'form':form})
    else:
       return HttpResponseRedirect('/login') 

def changeProfile(request):
    if request.user.is_authenticated:
        if request.POST:
            form = ChangeProfileFrm(request.POST, instance=request.user)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request,'Profile Update successfully')
                except Exception as e:
                    messages.error(request, e)
        else:
            form = ChangeProfileFrm(instance=request.user)
        return render(request, 'myapp/changeProfile.html', {'form':form})
    else:
        return HttpResponseRedirect('/login')


def appointmentHistory(request):
    if request.user.is_authenticated:
        myApp=Appointment.objects.raw("SELECT a.*, d.dname, s.days, s.time_slot FROM myapp_appointment a INNER JOIN myapp_doctor d ON  a.doctor_id=d.did INNER JOIN myapp_schedule s ON a.doctor_id=s.doctor_id WHERE a.user_id={}".format(request.user.id))
        return render(request, 'myapp/appointmentHistory.html', {'myapp':myApp})
    else:
        return HttpResponseRedirect('/login')
def contacts(request):
    return render(request, 'myapp/contacts.html')
def service(request):
    return render(request, 'myapp/service.html')