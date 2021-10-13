from django.conf.urls import include
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home),
    path('update/<int:id>', views.update),
    path('delete/<int:id>/', views.delete),
]