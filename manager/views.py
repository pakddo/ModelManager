# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Project, Model
from .forms import ProjectForm, ProjectEditForm, ModelForm, ModelEditForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project':project})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_edit.html', project)

def project_list(request):
    projects = Project.objects.all().order_by('-created_date')
    return render(request, 'project_list.html', {'projects':projects})

def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            username = None
            if request.user.is_authenticated():
                username = request.user.username
                user = get_user_model().objects.get(username=username)
            else:
                print "ERROR : No authenticated access"

            # form save (file_ location)
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('project_detail', pk=post.pk)
    else:
        form = ProjectForm()
        username = request.user.username
        user = get_user_model().objects.get(username=username)
    return render(request, 'project_edit.html', {'form': form, 'user':user})


def model_list(request, pk):
    project = get_object_or_404(Project, pk=pk)
    try:
        models = Model.objects.all().filter(project=project)
    except Frame.DoesNotExist:
        raise Http404("Frame does not exist")
    return render(request, 'model_list.html', {'project':project, 'models':models})

def model_detail(request, pk):
    model = get_object_or_404(Model, pk=pk)
    project = get_object_or_404(Project, pk=model.project_id)
    return render(request, 'model_detail.html', {'project':project,'model':model})

def model_edit(request, pk):
    model = get_object_or_404(Model, pk=pk)
    return render(request, 'model_edit.html', model)

def new_model(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ModelForm(request.POST, request.FILES)

        if form.is_valid():
            username = None
            if request.user.is_authenticated():
                username = request.user.username
                user = get_user_model().objects.get(username=username)
            else:
                print "ERROR : No authenticated access"

            # form save (file_ location)
            post = form.save(commit=False)
            post.project = project
            post.author = request.user
            post.save()
            return redirect('model_detail', pk=post.pk)
    else:
        form = ModelForm()
        username = request.user.username
        user = get_user_model().objects.get(username=username)
    return render(request, 'model_edit.html', {'form': form, 'user':user, 'project':project})


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
