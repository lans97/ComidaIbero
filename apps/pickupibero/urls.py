from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("menu/<str:rest_id>/", views.menu_view, name="menu"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
