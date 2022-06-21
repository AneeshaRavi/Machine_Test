from django import forms
from .models import Strings

class StringForm(forms.ModelForm):
    class Meta:
        model=Strings
        fields=('Master_String','String1','String2','String3','String4')
        widgets ={
           'Master_String':forms.TextInput(attrs={'class':'form-control'}),
           'String1':forms.TextInput(attrs={'class':'form-control'}),
           'String2':forms.TextInput(attrs={'class':'form-control'}),
           'String3':forms.TextInput(attrs={'class':'form-control'}),
           'String4':forms.TextInput(attrs={'class':'form-control'}),
            
        }
       