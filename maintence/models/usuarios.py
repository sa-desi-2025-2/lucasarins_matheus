from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha_hash = models.CharField(max_length=255)
    perfil_acesso = models.CharField(max_length=50)
    re = models.CharField(max_length=20, unique=True)

    class Meta:
        managed = False  # não criar ou alterar tabela
        db_table = 'usuarios'
        verbose_name = 'Usuário'

    def __str__(self):
        return f"{self.nome} ({self.id_usuario})"

    @staticmethod
    def get_from_user(user: User):
        """
        Retorna o objeto Usuarios vinculado a um user padrão do Django.
        Faz o vínculo pelo e-mail.
        """
        try:
            return Usuarios.objects.get(email=user.email)
        except Usuarios.DoesNotExist:
            return None