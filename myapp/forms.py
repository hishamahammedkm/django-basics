from django import forms
class DForm (forms.Form):
    email = forms.CharField(max_length=120,label='emaill',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20,label= 'enter password',widget=forms.Textarea(attrs={'class':'form-control'}))