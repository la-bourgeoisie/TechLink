from django.db import models


class AreaConhecimento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
