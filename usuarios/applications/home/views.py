import datetime

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse

class FechaMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super(FechaMixin,self).get_context_data(**kwargs)
        context["fecha"] = datetime.datetime.now() 
        return context
    


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users_app:login-user')
    
    
class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = 'home/mixin.html'
