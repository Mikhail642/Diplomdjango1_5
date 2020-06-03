from django import forms


class Organization(forms.Form):
    name_organization = forms.CharField()


class Project(forms.Form):
    name_project = forms.CharField()
    data_realizachii_s = forms.DateField()
    data_realizachii_po = forms.DateField()
    selka_na_saite = forms.CharField()
    product_innovation_deatelnosti = forms.CharField()
    rukovoditel_organization = forms.CharField()
    nauche_rukovoditel = forms.CharField()
    predloshenie_po_ispolzovanie = forms.CharField()
    name_organization = forms.ForeignKey()

class Function(forms.Form):
    function_v_projet = forms.CharField()

class Partner(forms.Form):
    name_partners = forms.CharField()


class PartnerVProject(forms.Form):
    parters = forms.ForeignKey(Partner, verbose_name='Партнеры', )
    project = forms.ForeignKey(Project, verbose_name='Проект', )
    function = forms.ForeignKey(Project, verbose_name='Функции')


class PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike(forms.Form):
    perspektive_ispolzovania_produkta_innovation_deitelnosti = forms.CharField()

class FunctionVProject(forms.Form):
    name_function = forms.CharField()
    id_function = forms.ForeignKey()


class PlanRealizachiiVProekte(forms.Form):
    zadacha = forms.CharField()
    project = forms.ForeignKey()
    kratoe_naimenovanie = forms.CharField()
    sroki_s = forms.DateField()
    sroki_po = forms.DateField()


class PrognozRazvitiaProekta(forms.Form):
    id_project = forms.ForeignKey()
    zadacha_prognoza = forms.CharField()
    name_product = forms.CharField()
    kratkoe_opisanie = forms.CharField()
    sroki_realizachii_s = forms.DateField()
    sroki_realizachii_po = forms.DateField()

