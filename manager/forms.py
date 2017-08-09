from django import forms
from .models import Project, Model


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        #self.fields['vid_file_loc'].required = False


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(ProjectEditForm, self).__init__(*args, **kwargs)

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        #self.fields['vid_file_loc'].required = False

class ModelEditForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(ModelEditForm, self).__init__(*args, **kwargs)
