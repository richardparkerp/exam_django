from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name="home"),
    path('signup/', SignUpView.as_view(),name="signup"),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(),name="verify"),
    path('login/', LoginView.as_view(),name="login"),
    path('about/', about,name="about"),
    path('contacts/', contacts,name="contacts"),
    path('home/', DoctorsList.as_view(),name="home"),
    path('home/doctor_detail/<int:pk>/', DoctorDetail.as_view(),name="doctor_detail"),
    path('appointment_create/', AppointmentCreate.as_view(),name="appointment_create"),
    ]