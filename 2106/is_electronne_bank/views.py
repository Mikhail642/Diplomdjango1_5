from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from is_electronne_bank.apps import Project
from is_electronne_bank.models import Project,Function,Organization,Partner,PartnerVProject,PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike
from is_electronne_bank.models import FunctionVProject, PlanRealizachiiVProekte,PrognozRazvitiaProekta

from is_electronne_bank.forms import ProjectForm,FunctionForm,OrganizationForm,PartnerForm,PartnerVProjectForm,PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm
from  is_electronne_bank.forms import FunctionVProjectForm, PlanRealizachiiVProekteForm, PrognozRazvitiaProektaForm
from .forms import  UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})




@login_required(login_url='/admin')

def project(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'post_list.html', {'project': project})


def index(request):
    project = Project.objects.filter(avtor=request.user)
    return render(request, 'display_organization.html', {'project': project})


def display_organization(request):
    organization = Organization.objects.all
    return render(request, 'display_organization.html', {'organization': organization})

def display_partner_organization(request):
    partner = Partner.objects.all
    return render(request, 'display_organization_partner.html',{'partner':partner})

def display_perspektive_ispolzovania(request):
    perspektive = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike.objects.all
    return render(request, 'display_perspektive.html',{'perspektive':perspektive})

def display_plan_realization(request):
    plan_realization = PlanRealizachiiVProekte.objects.all
    return render(request, 'display_plan_realization.html',{'plna_realization':plan_realization})

def display_prognoz_razvitia(request):
    prognoz_razvitia_proekta = PrognozRazvitiaProekta.objects.all
    return render(request, 'display_prognoz_razvitia.html',{'prognoz_razvitia_proekta':prognoz_razvitia_proekta})

def display_project(request):
     project = Project.objects.all
     return render(request, 'display_project.html', {'project': project})


def display_function(request):
    function = Function.objects.all
    return render(request, 'display_function.html', {'function': function})

def display_function_v_project(request):
    function_v_project = FunctionVProject.objects.all
    return render(request, 'display_function_v_project.html', {'function_v_project': function_v_project})



def project_new(request):
    if request.method == "POST":
            project.avtor = request.user
            project.save()
            return redirect('project_detail')
    else:
        form = ProjectForm()
    return render(request, 'project_edit.html', {'form': form})



def function_new(request):
    if request.method == "POST":
            Function.avtor = request.user
            Function.function_v_projet
            Function.save()
            return redirect('function_detail')
    else:
        form = FunctionForm()
    return render(request, 'function_edit.html', {'form': form})




def organization_new(request):
    if request.method == "POST":
        organization = Organization()
        organization.avtor = request.user
        organization.name_organization = request.POST.get('name_organization')
        organization.save()
        return redirect('/organization/detail/')
    else:
        form = OrganizationForm()
    return render(request, 'organization_edit.html', {'form': form})




def organization_edit(request, pk):
    post = get_object_or_404(Organization, pk=pk)
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=post)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.name_organization = request.name_organization
            organization.save()
            return redirect('organization_detail')
    else:
        form = OrganizationForm(instance=post)
    return render(request, 'organization_edit.html', {'form': form, 'post':post})

# в этом месте не правильно логика организованна.  detail должен принимать на вход id рганизации и выводить все данные по ней
def organization_detail(request):
    if request.method == "POST":
        organization = Organization()
        organization.avtor = request.user
        organization.save()
        return redirect('/organization/detail/')
    else:
        form = OrganizationForm()
    return render(request, 'organization_edit.html', {'form': form})


def partner_detail(request):
    if request.method == "POST":
        partner = Partner()
        partner.avtor = request.user
        partner.save()
        return redirect('/partners/detail/')
    else:
        form = PartnerForm()
    return render(request, 'partner_edit.html', {'form': form})



def partner_new(request):
    if request.method == "POST":
            partner = Partner()
            partner.avtor = request.user
            partner.name_partners = request.POST.get('name_partners')
            partner.save()
            return redirect('/partner_detail/')
    else:
        form = PartnerForm()
    return render(request, 'partner_edit.html', {'form': form})






def partner_v_project_new(request):
    if request.method == "POST":
            PartnerVProject.avtor = request.user
            PartnerVProject.save()
            return redirect('partner_v_project_detail')
    else:
        form = PartnerVProjectForm()
    return render(request, 'partner_v_project_edit.html', {'form': form})


def perspektive_new(request):
    if request.method == "POST":
            PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike.avtor = request.user
            PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike.save()
            return redirect('perspektive_detail')
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm()
    return render(request, 'perspektive_edit.html', {'form': form})



def function_v_project_new(request):
    if request.method == "POST":
            FunctionVProject.name_function = request.name_function
            FunctionVProject.id_function = request.id_function
            FunctionVProject.save()
            return redirect('function_v_project_detail')
    else:
        form = FunctionVProjectForm()
    return render(request, 'function_edit.html', {'form': form})




def plan_realiazation_v_project_new(request):
    if request.method == "POST":
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



