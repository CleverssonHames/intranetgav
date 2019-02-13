from django.db import models
from django.conf import settings

# Create your models here


class Linksites(models.Model):
	LOCAL_CHOICES =(
		('L','Loja'),
		('E','Escrtorio'),
	)
	TIPO_CHOICES = (
		('I','Interno'),
		('E','Externo'),
		('IE','Interno/Externo'),
	)
	titulo = models.CharField(verbose_name='titulo', max_length=50)
	site = models.CharField(u'site', max_length=50, blank=False)
	local = models.CharField(u'local', max_length=1, choices=LOCAL_CHOICES)
	tipo_acesso = models.CharField(u'tipo acesso', max_length=2, choices=TIPO_CHOICES)

	class Meta:
		verbose_name_plural = 'Links'


	def __str__(self):
		return self.titulo


class DeptosFiles(models.Model):
	DEPTO_CHOICES = (
		('1','RH'),
		('2','Dpto. Pessoal'),
		('3','Jurido'),
		('4','Financeiro'),
		('5','Fiscal'),
		('6','Contabilidade'),
		('7','Compras'),
		('8','Auditoria'),
		('9','MKT'),
		('10','Compras Indiretas'),
		('11','Patrimonio'),
		('12','TI'),
	)
	nome = models.CharField(max_length=50, verbose_name='nome do arquivo')
	descricao = models.TextField(verbose_name='descriçao do arquivo')
	arquivo = models.FileField(upload_to="media/")
	depto = models.CharField(u'Departamento', max_length=2, choices=DEPTO_CHOICES)

	class Meta:
		verbose_name_plural = 'Departamentos'

	def __str__(self):
		return self.nome


class Filial(models.Model):
	filial = models.CharField(max_length=15, verbose_name='Filial')
	bandeira = models.CharField(max_length=10, verbose_name='Bandeira')
	estado = models.CharField(max_length=2, verbose_name='Estado')
	cidade = models.CharField(max_length=50, verbose_name='cidade')
	bairro = models.CharField(max_length=50, verbose_name='Bairro')
	logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
	cep = models.CharField(max_length=11, verbose_name='CEP')
	cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
	tel_fixo = models.CharField(max_length=14, verbose_name='Tel. Fixo', blank=True)
	celular_1 = models.CharField(max_length=14, verbose_name='Celular 1', blank=True)
	celular_2 = models.CharField(max_length=14, verbose_name='Celular 2', blank=True)

	class Meta:
		verbose_name_plural = 'Filiais'

	def __str__(self):
		return self.filial


