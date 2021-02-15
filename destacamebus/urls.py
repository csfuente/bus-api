from django.contrib import admin
from django.urls import include, path
from control import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bus', views.BusViewSet)
router.register(r'chofer', views.ChoferViewSet)
router.register(r'trayecto', views.TrayectoViewSet)
router.register(r'pasajero', views.PasajeroViewSet)
router.register(r'asiento', views.AsientoViewSet)
router.register(r'horario', views.HorarioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index),
]