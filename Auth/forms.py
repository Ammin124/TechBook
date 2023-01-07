from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984','1985','1986', '1987', '1988', '1989','1990','1991', '1992','1993']

class SignUpFrom(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last Name'}))
    #phone = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact number'}))
    #birth = forms.DateField(label="Enter your birthday ", widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    #favorite_colors = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    #img = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label= ''
        self.fields['username'].help_text= ''

        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''

        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Con-Password'})
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''


class EditFrom(UserChangeForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last Name'}))
    #phone = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact number'}))
    #birth = forms.DateField(label="Enter your birthday ", widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    #img = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label= ''
        self.fields['username'].help_text= ''

