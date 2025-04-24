from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('<int:pk>/edit/', views.update_assignment, name='update_assignment'),  # Edit URL
    path('<int:pk>/delete/', views.delete_assignment, name='delete_assignment'),  # Delete URL
]