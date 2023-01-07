
from django import forms
from django.contrib.auth.models import User
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForms(forms.ModelForm):

    title = forms.CharField(label="Post Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    titleTag = forms.CharField(label="Post Title Tag", widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label="Your Post Descriptions", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'titleTag', 'author', 'category', 'body', 'image')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control', 'id': 'authorID', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
           # 'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EditForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ContactForms(forms.Form):
    name = forms.CharField(label="Full name", max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label="Enter your contact number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Please enter your email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label="Your valuable comments", widget=forms.Textarea(attrs={'class': 'form-control'}))