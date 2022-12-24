from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm
from .models import User
from .functions import code_generator

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    
    def form_valid(self,form):
        
        #Se genera codigo
        codigo = code_generator()
        #
        
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo,
        )
        
        # enviar codigo activacion
        asunto = 'Confirmacion de Email'
        mensaje = 'Codigo de verificacion ' + codigo
        email_remitente = 'angie.ryucond@gmail.com'
        #
        send_mail(asunto,mensaje,email_remitente,[form.cleaned_data['email']])
        #redirigir a pantalla de validacion
        
        return HttpResponseRedirect(
            reverse(
                'users_app:verify-user',
                kwargs={'pk': usuario.id}
            )
        )

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class LogoutUser(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login-user'
            )
        )
        
class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:login-user')
    login_url = reverse_lazy('users_app:login-user')
    
    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)
        return super(UpdatePassword,self).form_valid(form)
    
    
class CodeVerificationView(FormView):
    template_name = 'users/verify.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:login-user')
    
    
    
    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView,self).get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs
    
    def form_valid(self, form):
        
        User.objects.filter(
            id = self.kwargs['pk']
        ).update(
            is_active = True
        )
        
        return super(CodeVerificationView,self).form_valid(form)