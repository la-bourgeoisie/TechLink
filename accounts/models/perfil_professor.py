from django.db import models
from .custom_user import CustomUser
from .area_conhecimento import AreaConhecimento


class PerfilProfessor(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='professor_profile')
    formacao = models.TextField()
    apresentacao = models.TextField()
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    areas_conhecimento = models.ManyToManyField(AreaConhecimento, blank=True)

    def __str__(self):
        return self.usuario.nome
