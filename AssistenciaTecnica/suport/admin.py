from django.contrib import admin
from .models import Pessoa,FuncionarioSuporte,Funcionario,Departamento,Categoria,Chamada,Atendimento

admin.site.register(Pessoa)
admin.site.register(FuncionarioSuporte)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Categoria)
admin.site.register(Chamada)
admin.site.register(Atendimento)

# Register your models here.
