from django.db import models
from decimal import Decimal
from django.db.models import Sum
from django.conf import settings
from django.db import connection


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
    roi_calculado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    custo_total_peca = models.DecimalField(max_digits=12, decimal_places=2)
    anexos = models.CharField(max_length=255, blank=True, null=True)
    custo_mao_obra = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'reparos'
        verbose_name = 'Reparo'

    
    def custo_total(self):
        try:
            peca = Decimal(str(self.custo_total_peca)) if self.custo_total_peca else Decimal('0.00')
            mao = Decimal(str(self.custo_mao_obra)) if self.custo_mao_obra else Decimal('0.00')
            return peca + mao
        except Exception as e:
            print("ERRO AO CALCULAR CUSTO TOTAL:", e, self.custo_total_peca, self.custo_mao_obra)
            return Decimal('0.00')

    
    def calcular_roi(self, conservador_extensao_pct=0.10):
        try:
            ativo = self.id_ativo
            valor = Decimal(ativo.preco or 0)
            vida = Decimal(ativo.vida_util_esperada or 1)
            extensao = Decimal(self.extensao_vida_util or 0)
            custo = self.custo_total()  

            if custo <= 0:
                raise ValueError("O custo deve ser maior que zero")

           
            if extensao > vida:
                extensao = vida * Decimal(conservador_extensao_pct)

            if vida <= 0:
                vida = Decimal(1)

            ganho_estimado = (valor / vida) * extensao

            roi = ((ganho_estimado - custo) / custo) * 100

            return roi.quantize(Decimal("0.01"))

        except Exception as e:
            print("Erro no cálculo do ROI:", e)
            return None


    def save(self, *args, **kwargs):
        custo = self.custo_total()
    
        if custo <= 0:
            raise ValueError("RN001: Reparo deve ter custo total válido.")
    
        roi = self.calcular_roi()
        self.roi_calculado = roi if roi is not None else Decimal("0.00")
    
        super().save(*args, **kwargs)




    def __str__(self):
        return f"Reparo {self.id_reparo} - {self.id_ativo.nome}"
