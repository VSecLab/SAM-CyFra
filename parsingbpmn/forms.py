from django import forms

from .models import Process, System, Context, Profile


class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name']

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ["system_id"]
        fields = ['name','xml']

class ContextualizationForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = ['name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name', 'level', 'framework' ]
        exclude = ['context_id']

class FusionForm(forms.Form):
    actual_profile = forms.ModelChoiceField(queryset=Profile.objects.all(), empty_label="Select actual profile")
    target_profile= forms.ModelChoiceField(queryset=Profile.objects.all(), empty_label="Select target profile")

class SelectContextForm(forms.Form):
    contextualization_1= forms.ModelChoiceField(queryset=Context.objects.all(), empty_label="Select contextualization 1")
    contextualization_2= forms.ModelChoiceField(queryset=Context.objects.all(), empty_label="Select contextualization 2")





