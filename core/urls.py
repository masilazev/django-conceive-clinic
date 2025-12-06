from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a URL vazia ('') para a view login_view
    path('', views.login_view, name='login'),
]
