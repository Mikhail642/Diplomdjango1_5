from django.urls import path
from is_electronne_bank import views

urlpatterns = [
    path('', views.project, name='post_list'),
    path('Project/<int:pk>/', views.Project, name='post_list'),
]