from django.db import models

class Publicacoes(models.Model):
    titulo = models.CharField(max_length=100, help_text='Entre o titulo')
    data = models.DateField(help_text='Entre a data')
    texto = models.CharField(max_length= 100000, help_text='Entre sua publicação')

