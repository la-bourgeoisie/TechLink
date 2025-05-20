from django.db import models
from .custom_user import CustomUser


class PerfilAluno(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='aluno_profile')

    def __str__(self):
        return self.usuario.nome
