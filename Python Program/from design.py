from django import forms
class InputForm(forms.Form):
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
password = forms.CharField(widget = forms.PasswordInput())
from django.shortcuts import render
from .forms import InputForm
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)

    
<form action = "" method = "post">
	{% csrf_token %}
	{{form }}
	<input type="submit" value="Submit">
</form>


