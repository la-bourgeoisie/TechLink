from django.db import models
from .user import User


class PerfilAluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno_profile')

    def __str__(self):
        return self.usuario.nome
