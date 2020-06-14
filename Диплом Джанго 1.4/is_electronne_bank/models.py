from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Organization(models.Model):
    name_organization = models.CharField(max_length=200, verbose_name='Наименование организации')


    class Meta:
        verbose_name ='Организация'
        verbose_name_plural ='Организация'

class Project(models.Model):
    name_project = models.CharField(max_length=250, verbose_name='Наименование проекта', )
    data_realizachii_s = models.DateField(default=timezone.now, verbose_name='Дата реализации с', )
    data_realizachii_po = models.DateField(default=timezone.now, verbose_name='Дата реализации по', )
    selka_na_saite = models.CharField(max_length=250, null=True, blank=True, verbose_name='Ссылка на сайте')
    product_innovation_deatelnosti = models.CharField(max_length=250, verbose_name='Продукт инновационной деятельности')
    rukovoditel_organization = models.CharField(max_length=250, null=True, blank=True, verbose_name='Руководитель организации', )
    nauche_rukovoditel = models.CharField(max_length=250, null=True, blank=True, verbose_name='Научный руководитель',)
    predloshenie_po_ispolzovanie = models.CharField(max_length=250, null=True, blank=True, verbose_name='Предложения по использованию', )
    name_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Наименование организации')
    avtor = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Автор', related_name='project_avtor')

    class Meta:
      verbose_name ='Проекты'
      verbose_name_plural ='Проекты'


class Function(models.Model):
    function_v_projet = models.CharField(max_length=250, verbose_name='Функции в проекте')

    class Meta:
     verbose_name ='Функции'
     verbose_name_plural ='Функции'

class Partner(models.Model):
    name_partners = models.CharField(max_length=250, verbose_name='Название партнера')

    class Meta:
     verbose_name ='Организации-партнеры'
     verbose_name_plural ='Организации-партнеры'


class PartnerVProject(models.Model):
    parters = models.ForeignKey(Partner, verbose_name='Партнеры', on_delete=models.CASCADE, related_name="partners", )
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name="projec_partners", )
    function = models.ForeignKey(Project, verbose_name='Функции', on_delete=models.CASCADE,related_name="function_partner")

    class Meta:
        verbose_name ='Партнеры в проекте'
        verbose_name_plural ='Партнеры в проекте'

class PerspektiveIspolzovaniaRezultatovProektaVmassovoiPraktike(models.Model):
    perspektive_ispolzovania_produkta_innovation_deitelnosti = models.CharField(max_length=100, verbose_name='Перспективы использования')

    class Meta:
        verbose_name ='Перспективы использования проекта в массовой практике'
        verbose_name_plural ='Перспективы использования проекта в массовой практике'

class FunctionVProject(models.Model):
    name_function = models.CharField(max_length=100, verbose_name='Название функции', )
    id_function = models.ForeignKey(Project, verbose_name='Айди функции', on_delete=models.CASCADE,related_name="functionVproject", )

    class Meta:
        verbose_name ='Функции в проекте'
        verbose_name_plural='Функции в проекте'

class PlanRealizachiiVProekte(models.Model):
    zadacha = models.CharField(max_length=100, verbose_name='Задача', )
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE,related_name="plan_realizachiiVproekte", )
    kratoe_naimenovanie = models.CharField(max_length=100, verbose_name='Краткое наименование', )
    sroki_s = models.DateField(default=timezone.now, verbose_name='Сроки с', )
    sroki_po = models.DateField(default=timezone.now, verbose_name='Сроки по')

    class Meta:
        verbose_name ='План реализации проекта'
        verbose_name_plural = 'План реализации проекта'


class PrognozRazvitiaProekta(models.Model):
    id_project = models.ForeignKey(Project, verbose_name='Айди проекта', on_delete=models.CASCADE,related_name="prognoz_razvitia_projecta")
    zadacha_prognoza = models.CharField(max_length=100, verbose_name='Задача прогноза развития', )
    name_product = models.CharField(max_length=100, verbose_name='Название продукта', )
    kratkoe_opisanie = models.CharField(max_length=100, verbose_name='Краткое описание проекта', )
    sroki_realizachii_s = models.DateField(default=timezone.now, verbose_name='Сроки реализации с', )
    sroki_realizachii_po = models.DateField(default=timezone.now, verbose_name='Сроки реализации по')

    class Meta:
        verbose_name ='Прогноз развития проекта'
        verbose_name_plural ='Прогноз развития проекта'
