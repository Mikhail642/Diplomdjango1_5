from django import forms
from is_electronne_bank.models import Project
from is_electronne_bank.models import Organization
from is_electronne_bank.models import Partner
from is_electronne_bank.models import PartnerVProject
from is_electronne_bank.models import PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike
from is_electronne_bank.models import FunctionVProject
from is_electronne_bank.models import PlanRealizachiiVProekte
from is_electronne_bank.models import PrognozRazvitiaProekta
from is_electronne_bank.models import Function




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project','data_realizachii_s','data_realizachii_po','selka_na_saite',
      'product_innovation_deatelnosti','rukovoditel_organization','nauche_rukovoditel','predloshenie_po_ispolzovanie',
'name_organization','avtor']



class Project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_project','data_realizachii_s','data_realizachii_po','selka_na_saite',
      'product_innovation_deatelnosti','rukovoditel_organization','nauche_rukovoditel','predloshenie_po_ispolzovanie',
'name_organization','avtor']



class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name_organization']


class Organization(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name_organization']




class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ['function_v_projet']


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name_partners']


class FunctionVProjectForm(forms.ModelForm):
    class Meta:
        model = FunctionVProject
        fields = ['name_function','id_function']


class PartnerVProjectForm(forms.ModelForm):
    class Meta:
        model = PartnerVProject
        fields = ['parters','project','function']

class PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeForm(forms.ModelForm):
    class Meta:
        model =PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike
        fields = ['perspektive_ispolzovania_produkta_innovation_deitelnosti']



class PlanRealizachiiVProekteForm(forms.ModelForm):
    class Meta:
        model = PlanRealizachiiVProekte
        fields = ['zadacha','project','kratoe_naimenovanie','sroki_s','sroki_po']

class PrognozRazvitiaProektaForm(forms.ModelForm):
    class Meta:
        model = PrognozRazvitiaProekta
        fields =['id_project','zadacha_prognoza','name_product','kratkoe_opisanie','sroki_realizachii_s','sroki_realizachii_po']


