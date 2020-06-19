from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from is_electronne_bank.apps import Project
from is_electronne_bank.models import Project,Function,Organization,Partner,PartnerVProject,PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike
from is_electronne_bank.models import FunctionVProject, PlanRealizachiiVProekte,PrognozRazvitiaProekta

from is_electronne_bank.forms import ProjectForm,FunctionForm,OrganizationForm,PartnerForm,PartnerVProjectForm,PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm
from  is_electronne_bank.forms import FunctionVProjectForm, PlanRealizachiiVProekteForm, PrognozRazvitiaProektaForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
# from .forms import LoginForm, UserRegistrationForm

@login_required(login_url='/admin')

def project(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'post_list.html', {'project': project})

def display_organization(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'display_organization.html', {'project': project})

def index(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'index.html', {'project': project})



def project_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            project.avtor = request.user
            project.save()
            return redirect('project_detail')
    else:
        form = ProjectForm()
    return render(request, 'project_edit.html', {'form': form})



def function_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            Function.avtor = request.user
            Function.save()
            return redirect('function_detail')
    else:
        form = FunctionForm()
    return render(request, 'function_edit.html', {'form': form})




def organization_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            Organization.avtor = request.user
            Organization.save()
            return redirect('organizaton_detail')
    else:
        form = OrganizationForm()
    return render(request, 'organization_edit.html', {'form': form})





def partner_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            Partner.avtor = request.user
            Partner.save()
            return redirect('partner_detail')
    else:
        form = PartnerForm()
    return render(request, 'partner_edit.html', {'form': form})



def partner_v_project_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            PartnerVProject.avtor = request.user
            PartnerVProject.save()
            return redirect('partner_v_project_detail')
    else:
        form = PartnerVProjectForm()
    return render(request, 'partner_v_project_edit.html', {'form': form})


def perspektive_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike.avtor = request.user
            PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike.save()
            return redirect('perspektive_detail')
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm()
    return render(request, 'perspektive_edit.html', {'form': form})



def function_v_project_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
            FunctionVProject.name_function = request.name_function
            FunctionVProject.id_function = request.id_function
            FunctionVProject.save()
            return redirect('function_v_project_detail')
    else:
        form = FunctionVProjectForm()
    return render(request, 'function_edit.html', {'form': form})




def plan_realiazation_v_project_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
           PlanRealizachiiVProekte.zadacha = request.zadacha
           PlanRealizachiiVProekte.sroki_s = request.sroki_s
           PlanRealizachiiVProekte.sroki_po = request.sroki_po
           PlanRealizachiiVProekte.save()
           return redirect('plan_realization_v_project_detail')
    else:
        form = PlanRealizachiiVProekteForm()
    return render(request, 'plan_realization_edit.html', {'form': form})




def prognoz_razvitia_proekta_new(request):
    if request.method == "POST":
        #form = ProjectForm(request.POST)
        # if form.is_valid():
        #     # project = form.save(commit=False)
        #     project.name_project = request.name_project()
        #     project.data_realizachii_s = timezone.now()
        #     project.selka_na_saite = request.selka_na_saite()
        #     project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
        #     project.rukovoditel_organization = request.rukovoditel_organization()
        #     project.nauche_rukovoditel = request.nauche_rukovoditel()
        #     project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
        #     project.name_organization = request.name_organization()
           PrognozRazvitiaProekta.id_project = request.id_project
           PrognozRazvitiaProekta.zadacha_prognoza = request.zadacha_prognoza
           PrognozRazvitiaProekta.name_product = request.name_product
           PrognozRazvitiaProekta.kratkoe_opisanie =request.kratkoe_opisanie
           PrognozRazvitiaProekta.sroki_s = request.sroki_s
           PrognozRazvitiaProekta.sroki_po = request.sroki_po
           PrognozRazvitiaProekta.save()
           return redirect('prognoz_razvitia_proekta_detail')
    else:
        form = PlanRealizachiiVProekteForm()
    return render(request, 'plan_realization_edit.html', {'form': form})




#
# def project_edit(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if request.method == "POST":
#          form = ProjectForm(request.POST, instance=project)
#          if form.is_valid():
#              project = form.save(commit=False)
#              project.name_project = request.name_project()
#              project.data_realizachii_s = timezone.now()
#              project.selka_na_saite = request.selka_na_saite()
#              project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
#              project.rukovoditel_organization = request.rukovoditel_organization()
#              project.nauche_rukovoditel = request.nauche_rukovoditel()
#              project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
#              project.name_organization = request.name_organization()
#              project.avtor = request.avtor()
#              project.save()
#              return redirect('project_detail', pk=project.pk)
#     else:
#         form = ProjectForm(instance=project)
#     return render(request, 'project_edit.html', {'form': form})
#
#

