from django.db import models
from decimal import Decimal
from django.db.models import Sum
from django.conf import settings

class Reparos(models.Model):    
    id_reparo = models.AutoField(primary_key=True)
    id_ativo = models.ForeignKey('Ativos', db_column='id_ativo', on_delete=models.CASCADE)
    data_reparo = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo_parada_hora = models.IntegerField()
    extensao_vida_util = models.IntegerField()
    unid_extensao_vida_util = models.CharField(max_length=20)
    id_usuario = models.ForeignKey('Usuarios', db_column='id_usuario', on_delete=models.CASCADE, null=True, blank=True)
    roi_calculado = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total_peca = models.DecimalField(max_digits=12, decimal_places=2)
    anexos = models.CharField(max_length=255, blank=True, null=True)
    custo_mao_obra = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'reparos'
        verbose_name = 'Reparo'

    
    def custo_total(self):
        return (self.custo_total_peca or Decimal('0.00')) + (self.custo_mao_obra or Decimal('0.00'))

    def calcular_roi(self, conservador_extensao_pct=0.10):
        """
        Fórmula: ROI = (Ganho estimado - Custo) / Custo
        """
        try:
            ativo = self.id_ativo
            valor = Decimal(ativo.valor_inicial or 0)
            vida = Decimal(ativo.vida_util_esperada or 1)
            # Quando não informado, usa valor aproximado
            extensao = Decimal(self.extensao_vida_util or 0)
            if extensao == 0:
                extensao = vida * Decimal(conservador_extensao_pct) 
            ganho_estimado = (valor / vida) * extensao
            custo = self.custo_total()
            if custo == 0:
                return None
            roi = (ganho_estimado - custo) / custo


            return (roi.quantize(Decimal('.01')))
        except Exception:
            return None

    def save(self, *args, **kwargs):
        # Valida que  todo reparo deve ter custo total (peca + mão de obra)
        if (self.custo_total_peca is None or self.custo_total_peca == 0) and (self.custo_mao_obra is None or self.custo_mao_obra == 0):
            raise ValueError("RN001: Reparo deve ter custo total (peças e/ou mão de obra).")
        # Calculo ROI automatico
        self.roi_calculado = self.calcular_roi()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reparo {self.id_reparo} - {self.id_ativo.nome}"
