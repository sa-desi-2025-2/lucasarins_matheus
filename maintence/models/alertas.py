from django.db import models
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
