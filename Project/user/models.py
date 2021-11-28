from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, help_text='Entre com o seu nome')
    age = models.IntegerField(verbose_name='Idade',help_text= 'Entre com a sua idade')
    email = models.EmailField(help_text='Entre com o seu email') 

    def __str__(self): 
        return self.nome + ': ' + self.email
