from django.urls import path
from apps.aluno.views import index, listar, cadastrar, exibir, editar

urlpatterns = [
    path("", index, name="index"),
    path("lista", listar, name="aluno/lista"),
    path("cadastro", cadastrar, name="aluno/cadastro"),
    path("exibe", exibir, name="aluno/exibe"),
    path("edita", editar, name="aluno/edita")
]