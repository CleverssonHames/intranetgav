from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import PesquisaLojas
from django.http import Http404
from django.views.generic import DetailView

from .models import Linksites, DeptosFiles, Filial


# Create your views here.

def home(request):
	return render(request, 'intranet/home.html', {})

def links(request):
	linksite_lojas = Linksites.objects.filter(local='L')
	linksite_escritorio = Linksites.objects.filter(local='E')
	return render(request, 'intranet/links.html', {'linksite_lojas': linksite_lojas, 'linksite_escritorio':linksite_escritorio})

def departamento(request):
	ti = DeptosFiles.objects.filter(depto='12')
	return render(request, 'intranet/departamento.html', {'ti':ti})

def lojas(request):

	filtro_loja = request.GET.get('pesquisa', None)

	if filtro_loja:
		empresas = Filial.objects.filter(filial__icontains=filtro_loja)
	else:
		empresas = Filial.objects.all().order_by('filial')
	#estados = Filial.objects.values('estado').distinct()
	#cidades = Filial.objects.values('cidade').distinct()
	return render(request, 'intranet/lojas.html', {'empresas':empresas})

def empresa_avenida(request):
	empresas = Filial.objects.filter(bandeira='Avenida').order_by('filial')	
	return render(request, 'intranet/lojas.html', {'empresas': empresas})
	
def empresa_giovanna(request):
	empresas = Filial.objects.filter(bandeira='Giovanna').order_by('filial')
	return render(request, 'intranet/lojas.html', {'empresas': empresas })
	
def empresa_cd(request):
	empresas = Filial.objects.filter(bandeira='Deposito').order_by('filial')
	return render(request, 'intranet/lojas.html', {'empresas': empresas })
	
def empresa_esc(request):
	empresas = Filial.objects.filter(bandeira='Escritorio').order_by('filial')
	return render(request, 'intranet/lojas.html', {'empresas': empresas})
	
def teste(request):
	empresas = Filial.objects.all().order_by('filial')
	return render(request, 'intranet/testeform.html', {'empresas':empresas})


def etiqueta_correio(request):
	empresas = Filial.objects.all().order_by('filial')
	estados = Filial.objects.values('estado').distinct()
	cidades = Filial.objects.values('cidade').distinct()
	return render(request, 'intranet/etiqueta_correios.html', {'empresas':empresas, 'cidades': cidades, 'estados':estados})



def filtro(request, loja):
	loja = int(loja)
	empresas = Filial.objects.filter(id=loja)
	estados = Filial.objects.values('estado').distinct()
	cidades = Filial.objects.values('cidade').distinct()
	return render(request, 'intranet/lojas.html', {'empresas':empresas, 'cidades': cidades, 'estados':estados})

class detalhe(DetailView):
	template_name = 'intranet/filtro.html'
	model = Filial
	


