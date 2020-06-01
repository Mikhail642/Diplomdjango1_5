
from django.contrib import admin
from is_electronne_bank.models import Organization
from is_electronne_bank.models import Project
from is_electronne_bank.models import Function
from is_electronne_bank.models import Partner
from is_electronne_bank.models import PartnerVProject
from is_electronne_bank.models import PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike
from is_electronne_bank.models import FunctionVProject
from is_electronne_bank.models import PlanRealizachiiVProekte
from is_electronne_bank.models import PrognozRazvitiaProekta



class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["nameorganization"]
    list_display_links = ["nameorganization"]



class ProjectAdmin(admin.ModelAdmin):
    list_display = ["data_realizachii_s "]
    list_display_links = ["data_realizachii_s "]

    list_display = ["data_realizachii_po"]
    list_display_links = ["data_realizachii_po"]

    list_display = ["selka_na_saite"]
    list_display_links = ["selka_na_saite"]

    list_display = ["product_innovation_deatelnosti"]
    list_display_links = ["product_innovation_deatelnosti"]

    list_display = ["rukovoditel_organization"]
    list_display_links = ["rukovoditel_organization"]

    list_display = ["nauche_rukovoditel"]
    list_display =["nauche_rukovoditel"]

    list_display = ["predloshenie_po_ispolzovanie"]
    list_display_links =["predloshenie_po_ispolzovanie"]

    list_display =["name_organization"]
    list_display_links=["name_organization"]

class FunctionAdmin(admin.ModelAdmin):
    list_display =["function_v_projet"]
    list_display_links = ["function_v_projet"]

class PartnerAdmin(admin.ModelAdmin):
 list_display =["name_partners"]
 list_display_links = ["name_partners"]

 class PartnerVProjectAdmin(admin.ModelAdmin):

    list_display = ["project"]
    list_display_links = ["project"]


class PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeAdmin(admin.ModelAdmin):
    list_display = ["perspektive_ispolzovania_produkta_innovation_deitelnosti"]
    list_display_links = ["perspektive_ispolzovania_produkta_innovation_deitelnosti"]



class FunctionVProjectAdmin(admin.ModelAdmin):
    list_display = ["name_function"]
    list_display_links = ["id_function"]




class PlanRealizachiiVProekteAdmin(admin.ModelAdmin):
    list_display = ["zadacha"]
    list_display_links = ["zadacha"]

    list_display = ["project"]
    list_display_links = ["project"]

    list_display = ["kratoe_naimenovanie"]
    list_display_links = ["kratoe_naimenovanie"]

    list_display = ["sroki_s "]
    list_display_links = ["sroki_s "]


    list_display = ["sroki_po "]
    list_display_links = ["sroki_po"]


class PrognozRazvitiaProektaAdmin(admin.ModelAdmin):
    list_display = ["id_project"]
    list_display_links = ["id_project"]

    list_display = ["zadacha_prognoza"]
    list_display_links = ["zadacha_prognoza"]

    list_display = ["name_product"]
    list_display_links = ["name_product"]

    list_display = ["kratkoe_opisanie "]
    list_display_links = ["kratkoe_opisanie"]


    list_display = ["sroki_realizachii_s"]
    list_display_links = ["sroki_realizachii_s"]

    list_display = ["sroki_realizachii_po"]
    list_display_links = ["sroki_realizachii_po"]



admin.site.register(Organization, OrganizationAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Function, FunctionAdmin)

admin.site.register(Partner, PartnerAdmin)



admin.site.register( PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike, PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktikeAdmin)

admin.site.register( FunctionVProject,  FunctionVProjectAdmin)

admin.site.register( PlanRealizachiiVProekte, PlanRealizachiiVProekteAdmin)

admin.site.register(PrognozRazvitiaProekta, PrognozRazvitiaProektaAdmin)
