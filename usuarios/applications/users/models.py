from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    
    username = models.CharField('Usuario', max_length=10, unique=True)
    email = models.EmailField('Email', max_length=254)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    genero = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES, blank=True)
    
    USERNAME_FIELD = 'username'
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
    
    
    
