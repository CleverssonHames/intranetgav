from django.forms import ModelForm
from .models import Filial


class PesquisaLojas(ModelForm):
	class Meta:
		model = Filial
		fields = ['filial']
		

