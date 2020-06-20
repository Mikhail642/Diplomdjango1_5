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
    path('display_organization/', views.display_organization, name='display_organization'),
    path('display_partner_organization/',views.display_partner_organization, name='display_partner_organization'),
    path('display_perspektive_ispolzovania/',views.display_perspektive_ispolzovania,name='display_perspektive_ispolzovania'),
    path('display_plan_realization/',views.display_plan_realization,name='display_plan_realization'),
    path('display_prognoz_razvitia/', views.display_prognoz_razvitia, name='display_prognoz_razvitia'),
    path('display_project/', views.display_project, name='display_project'),
    path('display_function/', views.display_function, name='display_function'),
    path('display_function_v_project/', views.display_function_v_project, name='display_function_v_project'),

]
