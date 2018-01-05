
from  django import forms

class ProjectForm(forms.ModelForm):
    code = forms.IntegerField(label='Project Code:')
    name = forms.CharField(label='Project Name : ', max_length=32)
    