from django.contrib import admin

from .models import Categoriaativos, Ativos, Alertas,Usuarios,LogAuditorias


admin.site.register(Categoriaativos)
admin.site.register(Ativos)
admin.site.register(Alertas)
admin.site.register(Usuarios)
admin.site.register(LogAuditorias)
