from django.db import models
import pymysql

class Categoriaativos(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'categoriaativos'
        
    