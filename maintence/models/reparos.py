from django.db import models
class Reparos(models.Model):    
    id_reparo = models.AutoField(primary_key=True)
    id_ativo = models.ForeignKey('Ativos', db_column='id_ativo', on_delete=models.CASCADE)
    data_reparo = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo_parada_hora = models.IntegerField()
    extensao_vida_util = models.IntegerField()
    unid_extensao_vida_util = models.CharField(max_length=20)
    id_usuario = models.ForeignKey('Usuarios', db_column='id_usuario', on_delete=models.CASCADE)
    roi_calculado = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total_peca = models.DecimalField(max_digits=12, decimal_places=2)
    anexos = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Reparo {self.id_reparo} para {self.id_ativo.nome}"

    class Meta:
        managed = False
        db_table = 'reparos'
        verbose_name = 'Reparo'

