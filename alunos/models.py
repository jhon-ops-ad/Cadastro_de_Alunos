from django.db import models

# Create your models here.
#Conceito de ORM(não precisar de código sql para conectar,criar banco de dados)
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.nome