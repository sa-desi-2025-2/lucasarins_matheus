from django.db import models
class LogAuditorias(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', db_column='id_usuario', on_delete=models.CASCADE)
    id_ativo = models.ForeignKey('Ativos', db_column='id_ativo', on_delete=models.CASCADE)
    acao = models.CharField(max_length=100)
    tabela_afetada = models.CharField(max_length=100)
    id_reparo_afetado = models.CharField(max_length=50, blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Log {self.id_log} - Ação: {self.acao}"
    class Meta:
        managed = False
        db_table = 'logauditorias'
        verbose_name = 'Log de Auditoria'

