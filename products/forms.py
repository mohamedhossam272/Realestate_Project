from django import forms

class ContactSummaryForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Your Name is'
        }))
    
    email= forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Your Email'
        }))
    
    subject= forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Subject'
        }))
    
    message= forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Leave a message here'
        }))