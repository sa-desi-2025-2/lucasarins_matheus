from django.db import models
class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_empresa
    class Meta:
        managed = False
        db_table = 'fornecedores'
        verbose_name = 'Fornecedore'

