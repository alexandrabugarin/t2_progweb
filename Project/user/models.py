from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(
            email=email,
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            name,
            password=password,
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    name = models.CharField(verbose_name='Nome', max_length=100, help_text='Entre com o seu nome')
    age = models.IntegerField(verbose_name='Idade',help_text= 'Entre com a sua idade', null=True)
    email = models.EmailField(help_text='Entre com o seu email', unique=True) 
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def __str__(self): 
        return self.name + ': ' + self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
