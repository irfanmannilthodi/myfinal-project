from . models import Marvel,Dccomics,Monster
from django import forms



class dcform(forms.ModelForm):
    class Meta:
        model=Dccomics
        fields=['name','desc','img','year','cast']

class mcform(forms.ModelForm):
    class Meta:
        model=Monster
        fields=['name','desc','img','year','cast']

class marvelform(forms.ModelForm):
    class Meta:
        model=Marvel
        fields=['name','desc','img','year','cast']
