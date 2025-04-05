from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('completeTask/<int:pk>/', views.completeTask, name='completeTask'),
    path('markAsIncomplete/<int:pk>/', views.markAsIncomplete, name='markAsIncomplete'),
]