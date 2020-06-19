from django.template.defaulttags import url
from django.urls import path
from is_electronne_bank import views

urlpatterns = [
    path('', views.project, name='post_list'),
    path('project/<int:pk>/', views.Project, name='post_list'),
    path('project/new/', views.project_new, name='project_new'),
    path('function/new/', views.function_new, name='function_new'),
    path('organization/new/', views.organization_new, name='organization_new'),
    path('partner/new/', views.partner_new, name='partner_new'),
    path('partner_v_project/new/', views.partner_v_project_new, name='partner_v_project_new'),
    path('perspektive/new/', views.perspektive_new, name='perspektive_new'),
    path('function_v_project/new/', views.function_v_project_new, name='function_v_project_new'),
    path('plan_realization_v_project/new/', views.plan_realiazation_v_project_new, name='plan_realization_v_project_new'),
    path('prognoz_razvitia_proekta/new/', views.prognoz_razvitia_proekta_new, name='prognoz_razvitia_proekta'),
    path('',views.index, name='index'),
]
