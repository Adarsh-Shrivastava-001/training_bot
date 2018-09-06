from django import forms 

class train_form(forms.Form):
	que= forms.CharField(label='Question', max_length=500)