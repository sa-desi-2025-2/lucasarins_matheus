from django.contrib import admin

from .models import Categoriaativos, Ativos, Alertas,Usuarios,LogAuditorias, Fornecedores, Itens, Reparos, ItensReparo



admin.site.register(Categoriaativos)
admin.site.register(Ativos)
admin.site.register(Alertas)
admin.site.register(Usuarios)
admin.site.register(LogAuditorias)
admin.site.register(Fornecedores)
admin.site.register(Itens)
admin.site.register(Reparos)
admin.site.register(ItensReparo)
