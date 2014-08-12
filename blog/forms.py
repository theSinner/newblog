from django import forms

class News(forms.Form):
    title = forms.CharField()
    
