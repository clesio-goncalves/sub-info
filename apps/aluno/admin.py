from django.contrib import admin
from apps.aluno.models import Aluno

class ListandoAlunos(admin.ModelAdmin):
    list_display = ("id", "matricula", "nome", "telefone", "status")
    list_display_links = ("id", "matricula")
    search_fields = ("matricula", "nome")
    list_filter = ("status",) # adicionado
    list_per_page = 10

admin.site.register(Aluno, ListandoAlunos)