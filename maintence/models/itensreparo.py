from django.db import models

class ItensReparo(models.Model):
    id_itemreparo = models.AutoField(primary_key=True)
    id_item = models.ForeignKey('Itens', db_column='id_item', on_delete=models.CASCADE)
    id_reparo = models.ForeignKey('Reparos', db_column='id_reparo', on_delete=models.CASCADE)

    def __str__(self):
        return f"ItemReparo {self.id_itemreparo}"
    
    class Meta:
        managed = False
        db_table = 'itensreparo'
        verbose_name = 'Item de Reparo'