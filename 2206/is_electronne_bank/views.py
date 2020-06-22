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



def organization_detail(request):
    if request.method == "POST":
        organization = Organization()
        organization.avtor = request.user
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


def plan_realization_new(request):
    if request.method == "POST":
        plan_realization = Partner()
        plan_realization.avtor = request.user
        plan_realization.zadacha = request.POST.get('zadacha')
        plan_realization.project = request.POST.get('project')
        plan_realization.kratoe_naimenovanie = request.POST.get('kratoe_naimenovanie')
        plan_realization.sroki_s = request.POST.get('sroki_s')
        plan_realization.sroki_po = request.POST.get('sroki_po')
        plan_realization.save()
        return redirect('/plan_realization/detail/')
    else:
        form = PlanRealizachiiVProekteForm()
    return render(request, 'plan_realization_edit.html', {'form': form})





def plan_realization_edit(request, pk):
    post = get_object_or_404(PlanRealizachiiVProekte, pk=pk)
    if request.method == "POST":
        form = PlanRealizachiiVProekteForm(request.POST, instance=post)
        if form.is_valid():
            plan_realization = form.save(commit=False)
            plan_realization.zadacha = request('zadacha')
            plan_realization.project = request('project')
            plan_realization.kratoe_naimenovanie = request('kratoe_naimenovanie')
            plan_realization.sroki_s = request('sroki_s')
            plan_realization.sroki_po = request('sroki_po')
            plan_realization.save()
            return redirect('plan_realization_detail')
    else:
        form = PlanRealizachiiVProekteForm(instance=post)
    return render(request, 'plan_realization_edit.html', {'form': form, 'post':post})

def plan_realization_detail(request):
    if request.method == "POST":
        plan_realization = PlanRealizachiiVProekte()
        plan_realization.avtor = request.user
        plan_realization.save()
        return redirect('/plan_realization/detail/')
    else:
        form = PlanRealizachiiVProekteForm()
    return render(request, 'plan_realization_edit.html', {'form': form})



def partner_detail(request):
    if request.method == "POST":
        partner = Partner()
        partner.avtor = request.user
        partner.save()
        return redirect('/partner/detail/')
    else:
        form = PartnerForm()
    return render(request, 'partner_edit.html', {'form': form})

def partner_edit(request, pk):
    post = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=post)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.name_partners = request.name_partners
            partner.save()
            return redirect('partner_detail')
    else:
        form = PartnerForm(instance=post)
    return render(request, 'partner_edit.html', {'form': form, 'post':post})

def partner_new(request):
    if request.method == "POST":
        partner = Partner()
        partner.avtor = request.user
        partner.name_partners = request.POST.get('name_partners')
        partner.save()
        return redirect('/partner/detail/')
    else:
        form = PartnerForm()
    return render(request, 'partner_edit.html', {'form': form})






def perspektive_new(request):
    if request.method == "POST":
        perspektive = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike()
        perspektive.avtor = request.user
        perspektive.perspektive_ispolzovania_produkta_innovation_deitelnosti = request.POST.get('perspektive_ispolzovania_produkta_innovation_deitelnosti')
        perspektive.save()
        return redirect('/perspektive/detail/')
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm()
    return render(request, 'perspektive_edit.html', {'form': form})




def perspektive_edit(request, pk):
    post = get_object_or_404(PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike, pk=pk)
    if request.method == "POST":
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm(request.POST, instance=post)
        if form.is_valid():
            perspektive = form.save(commit=False)
            perspektive.perspektive_ispolzovania_produkta_innovation_deitelnosti = request.perspektive_ispolzovania_produkta_innovation_deitelnosti
            perspektive.save()
            return redirect('perspektive_detail')
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm(instance=post)
    return render(request, 'perspektive_edit.html', {'form': form, 'post':post})

def perspektive_detail(request):
    if request.method == "POST":
        perspektive = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike()
        perspektive.avtor = request.user
        perspektive.save()
        return redirect('/perspektive/detail/')
    else:
        form = PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm()
    return render(request, 'perspektive_edit.html', {'form': form})




def project_detail(request):
    if request.method == "POST":
        project = Project()
        project.avtor = request.user
        project.save()
        return redirect('/project/detail/')
    else:
        form = ProjectForm()
    return render(request, 'project_edit.html', {'form': form})

def project_edit(request, pk):
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            project = form.save(commit=False)
            project.name_organization = request.name_organization
            project.save()
            return redirect('project_detail')
    else:
        form = ProjectForm(instance=post)
    return render(request, 'project_edit.html', {'form': form, 'post':post})






def project_new(request):
    if request.method == "POST":
        project = Project()
        project.avtor = request.user
        project.name_organization = request.POST.get('name_organization')
        project.data_realizachii_s = request.POST.get('data_realizachii_s')
        project.data_realizachii_po = request.POST.get('data_realizachii_po')
        project.selka_na_saite = request.POST.get('selka_na_saite')
        project.product_innovation_deatelnosti = request.POST.get('product_innovation_deatelnosti')
        project.nauche_rukovoditel = request.POST.get('nauche_rukovoditel')
        project.predloshenie_po_ispolzovanie = request.POST.get('predloshenie_po_ispolzovanie')
        project.name_organization = request.POST.get('name_organization')
        project.provereno = request.POST.get('provereno')
        project.avtor = request.POST.get('avtor')
        project.save()
        return redirect('/project/detail/')
    else:
        form = ProjectForm()
    return render(request, 'project_edit.html', {'form': form})






def function_detail(request):
    if request.method == "POST":
        function = Function()
        function.avtor = request.user
        function.save()
        return redirect('/function/detail/')
    else:
        form = FunctionForm()
    return render(request, 'function_edit.html', {'form': form})

def function_edit(request, pk):
    post = get_object_or_404(Function, pk=pk)
    if request.method == "POST":
        form = FunctionForm(request.POST, instance=post)
        if form.is_valid():
            function = form.save(commit=False)
            function.name_function = request.name_function
            function.id_function = request.id_function
            function.save()
            return redirect('function_detail')
    else:
        form =FunctionForm(instance=post)
    return render(request, 'function_edit.html', {'form': form, 'post':post})

def function_new(request):
    if request.method == "POST":
        function = Function()
        function.avtor = request.user
        function.name_function = request.POST.get('name_function')
        function.save()
        return redirect('/function/detail/')
    else:
        form = FunctionForm()
    return render(request, 'function_edit.html', {'form': form})


def function_v_project_detail(request):
    if request.method == "POST":
        function_v_project = FunctionVProject()
        function_v_project.avtor = request.user
        function_v_project.save()
        return redirect('/function_v_project/detail/')
    else:
        form = FunctionVProjectForm()
    return render(request, 'function_v_project_edit.html', {'form': form})

def function_v_project_edit(request, pk):
    post = get_object_or_404(FunctionVProject, pk=pk)
    if request.method == "POST":
        form = FunctionVProjectForm(request.POST, instance=post)
        if form.is_valid():
            function_v_project = form.save(commit=False)
            function_v_project.name_function = request.name_function
            function_v_project.id_function = request.id_function
            function_v_project.save()
            return redirect('function_v_project_detail')
    else:
        form = FunctionVProjectForm(instance=post)
    return render(request, 'function_v_project_edit.html', {'form': form, 'post':post})

def function_v_project_new(request):
    if request.method == "POST":
        function_v_project = FunctionVProject()
        function_v_project.avtor = request.user
        function_v_project.name_function = request.POST.get('name_function')
        function_v_project.id_function = request.POST.get('id_function')
        function_v_project.save()
        return redirect('/function_v_project/detail/')
    else:
        form = FunctionVProjectForm()
    return render(request, 'function_v_project_edit.html', {'form': form})



def prognoz_razvitia_proekta_detail(request):
    if request.method == "POST":
        prognoz_razvitia_proekta = PrognozRazvitiaProekta()
        prognoz_razvitia_proekta.avtor = request.user
        prognoz_razvitia_proekta.save()
        return redirect('/prognoz_razvitia_proekta/detail/')
    else:
        form = PrognozRazvitiaProektaForm()
    return render(request, 'prognoz_razvitia_proekta_edit.html', {'form': form})

def prognoz_razvitia_proekta_edit(request, pk):
    post = get_object_or_404(PrognozRazvitiaProekta, pk=pk)
    if request.method == "POST":
        form = PrognozRazvitiaProektaForm(request.POST, instance=post)
        if form.is_valid():
            prognoz_razvitia_proekta = form.save(commit=False)
            prognoz_razvitia_proekta.zadacha_prognoza = request.zadacha_prognoza
            prognoz_razvitia_proekta.name_product = request.name_product
            prognoz_razvitia_proekta.kratkoe_opisanie = request.kratkoe_opisanie
            prognoz_razvitia_proekta.sroki_realizachii_s = request.sroki_realizachii_s
            prognoz_razvitia_proekta.sroki_realizachii_po = request.sroki_realizachii_po
            prognoz_razvitia_proekta.save()
            return redirect('prognoz_razvitia_proekta_detail')
    else:
        form = PrognozRazvitiaProektaForm(instance=post)
    return render(request, 'prognoz_razvitia_proekta_edit.html', {'form': form, 'post':post})

def prognoz_razvitia_proekta_new(request):
    if request.method == "POST":
        prognoz_razvitia_proekta = PrognozRazvitiaProekta()
        prognoz_razvitia_proekta.avtor = request.user
        prognoz_razvitia_proekta.zadacha_prognoza = request.POST.get('zadacha_prognoza')
        prognoz_razvitia_proekta.name_product = request.POST.get('name_product')
        prognoz_razvitia_proekta.kratkoe_opisanie = request.POST.get('kratkoe_opisanie')
        prognoz_razvitia_proekta.sroki_realizachii_s = request.POST.get('sroki_realizachii_s')
        prognoz_razvitia_proekta.sroki_realizachii_po = request.POST.get('sroki_realizachii_po')
        prognoz_razvitia_proekta.save()
        return redirect('/prognoz_razvitia/detail/')
    else:
        form =PrognozRazvitiaProektaForm()
    return render(request, 'prognoz_razvitia_proekta_edit.html', {'form': form})


