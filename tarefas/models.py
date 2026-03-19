from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('completa', 'Completa'),
        ('cancelada', 'Cancelada'),
        ('perdida', 'Perdida'),
    ]
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativa')

    def __str__(self):
        return self.titulo