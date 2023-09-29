from django.urls import path
from . import views

urlpatterns = [
    path('userlist/', views.get_data_view, name='get_data_view'),
    path('list/', views.kullanici_listesi, name='kullanici_listesi'),
]
