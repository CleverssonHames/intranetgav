from django.shortcuts import render
from django.db.models import Q
from .forms import PesquisaLojas

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
	empresas = Filial.objects.all().order_by('filial')
	estados = Filial.objects.values('estado').distinct()
	cidades = Filial.objects.values('cidade').distinct()
	return render(request, 'intranet/lojas.html', {'empresas':empresas, 'cidades': cidades, 'estados':estados})

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
	
def filtro_loja(resquest, pk):
	floja = Filial.objects.filter(pk=pk)
	return render(request, 'intranet/lojas.html', {'floja':floja})
	
def filtro_cidade(resquest, cidade):
	fcidade = Filial.objects.filter(cidade=cidade)
	return render(request, 'intranet/lojas.html', {'fcidade':fcidade})
	
def filtro_estado(resquest, estado):
	festado = Filial.objects.filter(estado=estado)
	return render(request, 'intranet/lojas.html', {'festado':festado})

def teste(request):
	empresas = Filial.objects.all().order_by('filial')
	estados = Filial.objects.values('estado').distinct()
	cidades = Filial.objects.values('cidade').distinct()
	return render(request, 'intranet/testeform.html', {'empresas':empresas, 'cidades': cidades, 'estados':estados})

def etiqueta_correio(request):
	return render(request, 'intranet/etiqueta_correios.html', {})
	# empresas = Filial.objects.all().order_by('filial')
	# estados = Filial.objects.values('estado').distinct()
	# cidades = Filial.objects.values('cidade').distinct()
	# return render(request, 'intranet/etiqueta_correio.html', {'empresas':empresas, 'cidades': cidades, 'estados':estados})


	
	
	



