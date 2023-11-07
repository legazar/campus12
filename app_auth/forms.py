from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "nom d'utilisateur",widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label= 'mot de passe',widget = forms.PasswordInput(attrs = {'class':'form-control'}))

class RegsiterForm(forms.Form):
    username = forms.CharField(label = "nom d'utilisateur",widget = forms.TextInput(attrs = {'class':'form-control'}))
    email = forms.CharField(label = "adresse email",widget = forms.EmailInput(attrs = {'class':'form-control'}) )
    password = forms.CharField(label= 'mot de passe',widget = forms.PasswordInput(attrs = {'class':'form-control'}))