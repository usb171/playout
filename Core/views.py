from django.http import JsonResponse
from django.shortcuts import render
from .API.amcp_pylib.core import *
from .API.amcp_pylib.module.query import *
from .API.amcp_pylib.module.basic import *
from .models import *
import json


client = Client()
client.connect("192.168.254.196", 5250)
flag_pause_resume = False


class Core:

    def index(request):
        template_name = "core/paginas/index.html"
        context = {}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)

    def index2(request):
        template_name = "core/paginas/index2.html"
        context = {}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)


class CoreAjax:

    def decklink(request):
        response = client.send(DECKLINK(video_channel=2, canal=1, format='1080i5994'))
        return JsonResponse({'response': str(response)})

    def play(request):
        id_midia = request.GET.get('id_midia')
        nome_arquivo = Midia.objects.get(id=id_midia).nome_arquivo

        print(id_midia, nome_arquivo)

        response = client.send(PLAY(video_channel=1, clip=nome_arquivo))
        return JsonResponse({'response': str(response)})

    def pause_resume(request):
        global flag_pause_resume
        if flag_pause_resume:
            response = client.send(PAUSE(video_channel=1))
            flag_pause_resume = not flag_pause_resume
        else:
            response = client.send(RESUME(video_channel=1))
            flag_pause_resume = not flag_pause_resume

        return JsonResponse({'response': str(response)})

    def stop(request):
        response = client.send(STOP(video_channel=1))
        return JsonResponse({'response': str(response)})

    def reconectar(request):
        global client
        client = Client()
        client.connect("192.168.254.196", 5250)
        return JsonResponse({'Flag': ''})

    def atualizar_ordem_payout(request):
        id = request.GET.get('id')
        ordem = request.GET.get('ordem')
        Midia_i.objects.filter(id=id).update(ordem=ordem)
        return JsonResponse({'erro':'', 'msg': 'Ordenado com sucesso!'})

    def carregar_tabela_playout(request):
        try:
            id_playout = request.GET.get('id_playout')
            playout = Playout.objects.get(id=id_playout)
            linhas = ""
            for midia in  Midia_i.objects.order_by("ordem").filter(playout=playout, ativo=True):
                linhas = linhas + "<tr id='{id}' data-id-midia='{id_midia}' class='clickableRow'>" \
                                    "<td> {titulo} </td>" \
                                    "<td> {duracao} </td>" \
                                  "</tr>".format(id=midia.id, id_midia=midia.midia.id, duracao=midia.midia.duracao, titulo=midia.midia.titulo)
            return JsonResponse({'linhas': linhas})
        except Exception as e:
            print(e)
            print("Problemas ao montar Playout")
            return JsonResponse({'erros': ''})