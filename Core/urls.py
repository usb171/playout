from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('index2', Core.index2, name='index2'),
    path('core_decklink_ajax', CoreAjax.decklink, name='core_decklink_ajax'),
    path('core_play_ajax', CoreAjax.play, name='core_play_ajax'),
    path('core_stop_ajax', CoreAjax.stop, name='core_stop_ajax'),
    path('core_pause_resume_ajax', CoreAjax.pause_resume, name='core_pause_resume_ajax'),
    path('core_reconectar_ajax', CoreAjax.reconectar, name='core_reconectar_ajax'),

    path('carregar_tabela_playout_ajax', CoreAjax.carregar_tabela_playout, name='carregar_tabela_playout_ajax'),
    path('atualizar_ordem_payout_ajax', CoreAjax.atualizar_ordem_payout, name='atualizar_ordem_payout_ajax'),
    path('listar_arquivos_servidor_ajax', CoreAjax.listar_arquivos_servidor, name='listar_arquivos_servidor_ajax'),
]
