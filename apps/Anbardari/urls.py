from django.urls import path
from . import views

urlpatterns = [
    path('anbardari/', views.ProductView.as_view())
]