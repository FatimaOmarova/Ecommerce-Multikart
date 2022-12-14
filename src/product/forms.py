from product.models import Review
from django import forms
from django.forms import ModelForm



class ProductReview(ModelForm):
   class Meta:
        model = Review 
        fields = ('product','name', 'email', 'title', 'content', 'rating')
        
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your  name','id':'name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email','id':'email'}),
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your  Review Subjects','id':'review'}),
			'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'','id':''}),
			'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your Message','id':'exampleFormControlTextarea1','rows':6}),
		}

