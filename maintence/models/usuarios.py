from django.db import models
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha_hash = models.CharField(max_length=255)
    perfil_acesso = models.CharField(max_length=50)
    re = models.CharField(max_length=20, unique=True)

    def __str__(self):
         return f" {self.nome} - {self.id_usuario}"
    
    class Meta:
        managed = False
        db_table = 'usuarios'
        verbose_name = 'Usuário'

