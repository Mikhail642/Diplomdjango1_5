from django.urls import path
from is_electronne_bank import views

urlpatterns = [
    path('', views.project, name='post_list'),
    path('project/<int:pk>/', views.Project, name='post_list'),
    path('project/<int:pk>/edit/', views.project_edit,name='project_edit'),
    path('project/new/', views.project_new, name='project_new'),
]

