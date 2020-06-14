
from django.urls import path
from . import views




urlpatterns = [
    path('', views.Project, name='post_list'),
    path('Project/<int:pk>/', views.Project, name='post_list'),
    path('Project/new/', views.Project, name='Project_new'),
]

path('Project/<int:pk>/edit/', views.Project_edit, name='Project_edit'),

