from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nome, senha, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','sobrenome','tipo']

    groups = models.ManyToManyField(
        Group,
        related_name='+',
        blank=True,
        help_text='Grupos aos quais este usuário pertence.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='+',
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='permissões do usuário',
    )

    def __str__(self):
        return f'{self.nome} ({self.tipo})'
