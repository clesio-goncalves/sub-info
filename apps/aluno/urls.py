from django.urls import path
from apps.aluno.views import listar, cadastrar, exibir, editar

urlpatterns = [
    path("lista", listar, name="aluno/lista"),
    path("cadastro", cadastrar, name="aluno/cadastro"),
    path("exibe/<int:id>", exibir, name="aluno/exibe"),
    path("edita/<int:id>", editar, name="aluno/edita")
]