from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from is_electronne_bank.apps import Project
from is_electronne_bank.models import Project
from is_electronne_bank.forms import ProjectForm
from django.utils import timezone

@login_required(login_url='/admin')

def project(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'post_list.html', {'project': project})


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.name_project = request.name_project()
            project.data_realizachii_s = timezone.now()
            project.selka_na_saite = request.selka_na_saite()
            project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
            project.rukovoditel_organization = request.rukovoditel_organization()
            project.nauche_rukovoditel = request.nauche_rukovoditel()
            project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
            project.name_organization = request.name_organization()
            project.avtor = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'templates/project_edit.html', {'form': form})





def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
         form = ProjectForm(request.POST, instance=project)
         if form.is_valid():
             project = form.save(commit=False)
             project.name_project = request.name_project()
             project.data_realizachii_s = timezone.now()
             project.selka_na_saite = request.selka_na_saite()
             project.product_innovation_deatelnosti = request.product_innovation_deatelnosti()
             project.rukovoditel_organization = request.rukovoditel_organization()
             project.nauche_rukovoditel = request.nauche_rukovoditel()
             project.predloshenie_po_ispolzovanie = request.predloshenie_po_ispolzovanie()
             project.name_organization = request.name_organization()
             project.avtor = request.avtor()
             project.save()
             return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'templates/project_edit.html', {'form': form})