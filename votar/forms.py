from django import forms

class CreatePartido(forms.Form):
	nombre = forms.CharField(label='El nombre del partido', max_length=255, required=True, widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
	bandera = forms.ImageField(required=True, widget=forms.FileInput(attrs={'required': True, 'class': 'form-control'}))
	slogan = forms.CharField(label='Slogan del partido', max_length=255, required=True, widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))

class CreateEstudiante(forms.Form):
	nombre = forms.CharField(label='El nombre del estudiante', max_length=255, required=True, widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
	cedula = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
	do_vote = forms.BooleanField(required=False)
	CHOICES = (
		(1, 'Masculino'),
		(0, 'Femenino'),
	)
	gender = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
