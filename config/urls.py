
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from maintence.views import CategoriaativosViewSet

router = DefaultRouter()
router.register(r'categoriaativos', CategoriaativosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
