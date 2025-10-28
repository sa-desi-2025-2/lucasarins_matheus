from django.db import models
import pymysql

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
        
class Ativos(models.Model):
    id_ativo = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey('Categoriaativos', db_column='id_categoria', on_delete=models.CASCADE)
    codigo_ativo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
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

class Alertas(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    id_ativo = models.ForeignKey('Ativos', db_column='id_ativo', on_delete=models.CASCADE)
    tipo_alerta = models.CharField(max_length=50)
    limiar_porcentagem = models.DecimalField(max_digits=5, decimal_places=2)
    limiar_roi = models.DecimalField(max_digits=10, decimal_places=2)
    status_alerta = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f"Alerta {self.tipo_alerta} para {self.id_ativo.nome}"
    class Meta:
        managed = False
        db_table = 'alertas'
        verbose_name = 'Alerta'

