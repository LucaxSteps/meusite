from django.urls import path
from .views import (
    IndexView, ListarEdicoesView, ExibirEdicaoView, ExibirNoticiaView,
    CadastrarEdicaoView, CadastrarNoticiaView, PesquisarView
)
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('edicoes/', ListarEdicoesView.as_view(), name='listar_edicoes'),
    path('edicoes/<int:edicao_id>/', ExibirEdicaoView.as_view(), name='exibir_edicao'),
    path('noticias/<int:noticia_id>/', ExibirNoticiaView.as_view(), name='exibir_noticia'),
    path('cadastrar/edicao/', CadastrarEdicaoView.as_view(), name='cadastrar_edicao'),
    path('cadastrar/noticia/', CadastrarNoticiaView.as_view(), name='cadastrar_noticia'),
    path('pesquisar/', PesquisarView.as_view(), name='pesquisar'),
    path('register/', views.Cadastro, name='cadastro'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
