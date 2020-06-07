from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from is_electronne_bank.apps import Project
from is_electronne_bank.models import Project



@login_required(login_url='/admin')

def project(request):
    project = get_object_or_404(Project, pk=1)
    return render(request, 'post_list.html', {'project': project})



