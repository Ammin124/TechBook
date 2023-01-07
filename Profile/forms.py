from django import forms
from .models import Profile

class EditProfileForms(forms.ModelForm):
    bio = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ('avatar', 'bio')

        widgets = {
            #'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }