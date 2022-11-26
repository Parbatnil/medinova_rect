from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('about', views.about, name="about-page"),
    path('reg', views.userReg, name="reg-page"),
    path('login', views.userLog, name="log-page"),
    path('logout', views.userLogout, name="logout-page"),
    path('profile', views.profile, name="profile-page"),
    path('chngpro', views.changeProfile, name="chngpro-page"),
    path('appoint/<did>', views.makeAppoint, name="appoint-page"),
    path('apphistory', views.appointmentHistory, name="apphis-page"),
    path('contacts', views.contacts, name="contacts-page"),
    path('service', views.service, name="service-page"),
]