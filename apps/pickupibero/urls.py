from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("menu/<str:rest_id>/", views.menu_view, name="menu"),
    path("producto/<str:producto_id>/", views.producto_view, name="producto"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("agregar-a-carrito/", views.agregar_a_carrito, name="agregar-a-carrito"),
    path("carrito/", views.carrito_view, name="carrito"),
    path('borrar-del-carrito/<str:numItem>/', views.borrar_del_carrito, name='borrar-del-carrito'),
    path("comprar-carrito/", views.comprar_carrito, name="comprar-carrito"),
    path("orden-creada/", views.orden_creada, name="orden-creada"),
]
