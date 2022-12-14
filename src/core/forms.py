from django import forms
from django.forms import ModelForm
from core.models import Subscribers, Contact
from django.forms.widgets import TextInput, Textarea, EmailInput
# class Contact(forms.Form):
#     first_name = forms.CharField(
#         max_length=128,
#         label="",
#         widget=forms.TextInput(attrs={"placeholder": "Enter your First name",
#         'class':'form-control',
#         'id':'name'        
#         }),
#     )
#     last_name = forms.CharField(
#         max_length=128,
#         label="",
#         widget=forms.TextInput(attrs={"placeholder": "Enter your Last name",
#         'class':'form-control',
#         'id':'last-name'
#         }),
#     )
#     email = forms.EmailField(
#         max_length=128,
#         label="",
#         widget=forms.EmailInput(attrs={"placeholder": "Enter your Email",
#         'class':'form-control',
#         'id':'email'
#         }),
#     )
#     phone_number = forms.CharField(
#         max_length=128,
#         label="",
#         widget=forms.NumberInput(attrs={"placeholder": "Enter your Phone number",
#         'class':'form-control',
#         'id':'review'
#         }),
#     )
#     description = forms.CharField(
#         label="",
#         widget=forms.Textarea(attrs={"placeholder": "Write Your Message",
#         'class':'form-control',
#         'id':'exampleFormControlTextarea1',
#         'rows':'6'
#         }),
#     )


class ContactForm(ModelForm):

   class Meta:
        model = Contact 
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'description')
        
        widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your First name','id':'name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Last name','id':'last-name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email','id':'email'}),
			'phone_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your Phone number','id':'review'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your Message','id':'exampleFormControlTextarea1','rows':6}),
		}



class Subscribe(ModelForm):
    email = forms.CharField(max_length=50, widget= EmailInput(
        attrs={'required': 'true', 'placeholder': 'Enter Your email', 'class': 'form-control', 'id': 'email',
               'onfocus': "this.value=''"}))

    class Meta:
        model = Subscribers
        fields = ['email']
