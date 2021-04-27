from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # post/<int:pk>/ especifica un patrón de URL, 
    # URL denominada post_detail que hace referencia a una vista llamada view.post_detail
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]