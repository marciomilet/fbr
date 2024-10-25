from django.urls import path
from .views import EmpresaAPIView

urlpatterns = [
    path('empresa/', EmpresaAPIView.as_view())
]