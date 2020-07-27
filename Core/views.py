from django.http import JsonResponse
from django.shortcuts import render
from .tools.casparCG import *

casparGC = CasparGC()

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
        return JsonResponse({'response': casparGC.decklink(request)})

    def play(request):
        return JsonResponse({'response':casparGC.play(request)})

    def pause_resume(request):
        return JsonResponse({'response': casparGC.pause_resume(request)})

    def stop(request):
        return JsonResponse({'response': casparGC.stop(request)})

    def reconectar(request):
        return JsonResponse({'response': casparGC.reconectar(request)})

    def atualizar_ordem_payout(request):
        return JsonResponse({'response':casparGC.atualizar_ordem_payout(request)})

    def carregar_tabela_playout(request):
        return JsonResponse(casparGC.carregar_tabela_playout(request))

    def listar_arquivos_servidor(request):
        return JsonResponse({'arquivos': casparGC.listar_arquivos_servidor(request)})
