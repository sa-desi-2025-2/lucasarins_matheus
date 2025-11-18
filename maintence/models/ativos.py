from django.db import models
class Ativos(models.Model):
    id_ativo = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey('Categoriaativos', db_column='id_categoria', on_delete=models.CASCADE)
    codigo_ativo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    data_aquisicao = models.DateField()
    vida_util_esperada = models.IntegerField()
    unid_vida_util = models.CharField(max_length=20)
    localizacao = models.CharField(max_length=150)
    depreciacao_anual = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'ativos'
        verbose_name = 'Ativo'