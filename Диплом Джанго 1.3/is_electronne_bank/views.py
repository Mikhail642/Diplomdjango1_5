from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request
from pbr.tests.testpackage.doc.source.conf import project

from is_electronne_bank.apps import Project



@login_required(login_url='/admin')
def post_list(request):
    Project.objects.filter(avtor=request.user)
    return render(request, 'is_electronne_bank/post_list.html', {'Project': project})



