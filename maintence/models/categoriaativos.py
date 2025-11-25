from django.db import models

class Categoriaativos(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.nome_categoria

    class Meta:
        managed = False
        db_table = 'categoriaativos'
        verbose_name = 'Categoria de Ativo'
         