from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('links', views.links, name='links'),
   path('departamento', views.departamento, name='departamento'),
   path('lojas', views.lojas, name='lojas'),
   path('empresa_avenida', views.empresa_avenida, name='empresa_avenida'),
   path('empresa_giovanna', views.empresa_giovanna, name='empresa_giovanna'),
   path('empresa_cd', views.empresa_cd, name='empresa_cd'),
   path('empresa_esc', views.empresa_esc, name='empresa_esc'),
   path('teste', views.teste, name='teste'),
   path('etiqueta_correio', views.etiqueta_correio, name='etiqueta_correio'),
   path('filtro/<int:id>', views.filtro, name='filtro'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)