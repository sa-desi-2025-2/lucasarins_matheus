from django.db import models
class Itens(models.Model):
    id_item = models.AutoField(primary_key=True)
    nome_peca = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    id_fornecedor = models.ForeignKey('Fornecedores', db_column='id_fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_peca
    class Meta:
        managed = False
        db_table = 'itens'
        verbose_name = 'Iten'
