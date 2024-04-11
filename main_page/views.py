from django.shortcuts import render
from .models import Doctor,Appointment
from .forms import DoctorForm, AppointmentForm,SignUpForm
from django.views import View
from django.views.generic import CreateView,ListView,DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin




class SignUpView(SuccessMessageMixin, CreateView):
    model=User
    form_class=SignUpForm
    template_name = 'main_page/signup.html'
    success_url = reverse_lazy('home')
    success_message = 'Пользователь успешно создан'


    def send_verification_email(self,user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}! pleace click the link below to verify your email \n\n {verify_url}'
        send_mail(subject,message,'isabayev.b.03@gmail.com',[user.email])


    def form_valid(self,form):
        response = super().form_valid(form)
        user = self.object 
        user.is_active = False
        user.save()
        self.send_verification_email(self.object)
        return response 
    


class VerifyEmailView(View):
    def get(self,request,user_pk,token):
        user = User.objects.get(pk= user_pk)
        if default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(request,'Your email has been verified')
            return redirect(reverse('home'))
        else:
            messages.error(request,'Invalid verification link')
            return redirect(reverse('home'))



class LoginView(SuccessMessageMixin,LoginView):
    template_name = 'main_page/login.html'
    next_page = reverse_lazy('home')
    success_message = 'You are loged in successfully'








class DoctorsList(ListView):
    model = Doctor
    template_name = 'main_page/home.html'
    context_object_name = 'doctors'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'main_page/doctor_detail.html'
    form = AppointmentForm
    context_object_name = 'doctor'
    
    def get_context_data(self, **kwargs):
        context = super(DoctorDetail, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = self.object
            appointment.save()
            return redirect(reverse_lazy('doctor_detail', kwargs={'pk': self.object.pk}))
        return self.render_to_response(self.get_context_data(form=form))
    

    

class AppointmentCreate(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'main_page/appointment_create.html'
    success_url = reverse_lazy('home')


def index(request):
    return render(request, 'main_page/layout.html')

def about(request):
    return render(request, 'main_page/about.html')

def home(request):
    return render(request, 'main_page/home.html')

def contacts(request):
    return render(request, 'main_page/contacts.html')