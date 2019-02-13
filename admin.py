from django.contrib import admin

from .models import Linksites, DeptosFiles, Filial

# Register your models here.

#class LinksAdmin(admin.ModelAdmin):
#	pass

admin.site.register(Linksites)
admin.site.register(DeptosFiles)
admin.site.register(Filial)

