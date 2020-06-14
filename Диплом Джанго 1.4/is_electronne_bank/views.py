from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import request, HttpResponse

from is_electronne_bank.forms import Project, ProjectForm,OrganizationForm,PartnerForm
from is_electronne_bank.forms import PartnerVProjectForm
from is_electronne_bank.forms import PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm
from is_electronne_bank.forms import FunctionVProjectForm,FunctionForm
from is_electronne_bank.forms import PlanRealizachiiVProekteForm

from is_electronne_bank.forms import PrognozRazvitiaProektaForm

@login_required(login_url='/admin')
def post_list(request):
    project = Project.objects.filter(avtor=request.user)
    form = ProjectForm()
    return render(request, 'post_list.html', {'project': project,'form':form})



def Project_edit(request, pk):
    Project = get_object_or_404(ProjectForm, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=Project)
        if form.is_valid():
            Project = form.save(commit=False)
            ProjectForm.name_project = request.name_project()
            ProjectForm.data_realizachii_s = timezone.now()
            ProjectForm.data_realizachii_po = timezone.now()
            ProjectForm.selka_na_saite = request.selka_na_saite()
            ProjectForm.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
            ProjectForm.rukovoditel_organization = request.rukovoditel_organization()
            ProjectForm.nauche_rukovoditel = request.nauche_rukovoditel()
            ProjectForm.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
            ProjectForm.name_organization = request.name_organization()
            ProjectForm.avtor = request.avtor()
            Project.save()
            return redirect('Project_detail', pk=ProjectForm.pk)
    else:
        form = ProjectForm(instance=Project)
    return render(request, 'templates/post_list.html', {'form': form})


def Organization_edit(request, pk):
    Organization = get_object_or_404(OrganizationForm, pk=pk)
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=Organization)
        if form.is_valid():
            Organization = form.save(commit=False)
            OrganizationForm.name_organization = request.name_organization()
            Organization.save()
            return redirect('Organization_detail', pk=OrganizationForm.pk)
    else:
        form = OrganizationForm(instance=Organization)
    return render(request, 'templates/post_list.html', {'form': form})

def Function_edit(request, pk):
    Function = get_object_or_404(FunctionForm, pk=pk)
    if request.method == "POST":
        form = FunctionForm(request.POST, instance=Function)
        if form.is_valid():
            Function = form.save(commit=False)
            FunctionForm.function_v_projet = request.functon_v_project()
            Function.save()
            return redirect('Function_detail', pk=FunctionForm.pk)
    else:
        form = FunctionForm(instance=Function)
    return render(request, 'templates/post_list.html', {'form': form})

def Partner_edit(request, pk):
    Partner = get_object_or_404(PartnerForm, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=Partner)
        if form.is_valid():
            Partner = form.save(commit=False)
            PartnerForm.name_partners = request.name_partners()
            Partner.save()
            return redirect('Partner_detail', pk=PartnerForm.pk)
    else:
        form = FunctionForm(instance=Partner)
    return render(request, 'templates/post_list.html', {'form': form})


def FunctionVproject_edit(request, pk):
    FunctionVProject = get_object_or_404(FunctionVProjectForm, pk=pk)
    if request.method == "POST":
        form = FunctionVProject(request.POST, instance=FunctionVProject)
        if form.is_valid():
            FunctionVProject = form.save(commit=False)
            FunctionVProjectForm.id_function = request.id_function()
            FunctionVProjectForm.name_function = request.name_function()
            FunctionVProject.save()
            return redirect('FunctionVProject_detail', pk=FunctionVProjectForm.pk)
    else:
        form = FunctionForm(instance=FunctionVProject)
    return render(request, 'templates/post_list.html', {'form': form})


def PartnerVProject_edit(request, pk):
    PartnerVProject = get_object_or_404(PartnerVProjectForm, pk=pk)
    if request.method == "POST":
        form = PartnerVProject(request.POST, instance=PartnerVProject)
        if form.is_valid():
            PartnerVProject = form.save(commit=False)
            PartnerVProjectForm.parters = request.parters()
            PartnerVProjectForm.project = request.project()
            PartnerVProjectForm.function = request.function()
            PartnerVProject.save()
            return redirect('PartnerVProject_detail', pk=PartnerVProjectForm.pk)
    else:
        form = PartnerVProjectForm(instance=PartnerVProject)
    return render(request, 'templates/post_list.html', {'form': form})


def PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike_edit(request, pk):
    PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike = get_object_or_404(PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm, pk=pk)
    if request.method == "POST":
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike(request.POST, instance=PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike)
        if form.is_valid():
            FunctionVProject = form.save(commit=False)
            FunctionVProjectForm.id_function = request.id_function()
            FunctionVProjectForm.name_function = request.name_function()
            FunctionVProject.save()
            return redirect('FunctionVProject_detail', pk=FunctionVProjectForm.pk)
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm(instance=PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike)
    return render(request, 'templates/post_list.html', {'form': form})

def PlanRealizachiiVProekte_edit(request, pk):
    PlanRealizachiiVProekte = get_object_or_404(PlanRealizachiiVProekteForm, pk=pk)
    if request.method == "POST":
        form = PlanRealizachiiVProekte(request.POST, instance=PlanRealizachiiVProekte)
        if form.is_valid():
            PlanRealizachiiVProekte = form.save(commit=False)
            PlanRealizachiiVProekteForm.parters = request.parters()
            PlanRealizachiiVProekteForm.zadacha = request.zadacha()
            PlanRealizachiiVProekteForm.project = request.project()
            PlanRealizachiiVProekteForm.kratoe_naimenovanie = request.kratoe_naimenovanie()
            PlanRealizachiiVProekteForm.sroki_s = request.sroki_s()
            PlanRealizachiiVProekteForm.sroki_po = request.sroki_po()
            PlanRealizachiiVProekte.save()
            return redirect('FunctionVProject_detail', pk=PlanRealizachiiVProekteForm.pk)
    else:
        form = PlanRealizachiiVProekteForm(instance=PlanRealizachiiVProekte)
    return render(request, 'templates/post_list.html', {'form': form})

def PrognozRazvitiaProekta_edit(request, pk):
    PrognozRazvitiaProekta = get_object_or_404(PrognozRazvitiaProektaForm, pk=pk)
    if request.method == "POST":
        form = PrognozRazvitiaProekta(request.POST, instance=PrognozRazvitiaProekta)
        if form.is_valid():
            PrognozRazvitiaProekta = form.save(commit=False)
            PrognozRazvitiaProektaForm.id_project = request.id_project()
            PrognozRazvitiaProektaForm.zadacha_prognoza = request.zadacha_prognoza()
            PrognozRazvitiaProektaForm.name_product = request.name_product()
            PrognozRazvitiaProektaForm.kratkoe_opisanie = request.kratkoe_opisanie()
            PrognozRazvitiaProektaForm.sroki_realizachii_s = request.sroki_realizachii_s()
            PrognozRazvitiaProektaForm.sroki_realizachii_po = request.sroki_realizachii_po()
            PrognozRazvitiaProekta.save()
            return redirect('PrognozRazvitiaProekta_detail', pk=PrognozRazvitiaProektaForm.pk)
    else:
        form = PrognozRazvitiaProektaForm(instance=PrognozRazvitiaProekta)
    return render(request, 'templates/post_list.html', {'form': form})

