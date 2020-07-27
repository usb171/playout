from ..API.amcp_pylib.core import *
from ..API.amcp_pylib.module.query import *
from ..API.amcp_pylib.module.basic import *
from ..models import *


class CasparGC():

    def __init__(self, servidor="localhost", porta=5250):
        self.client = Client()
        self.client.connect(servidor, porta)
        self.flag_pause_resume = False

    def decklink(self, request):
        response = self.client.send(DECKLINK(video_channel=2, canal=1, format='1080i5994'))
        return str(response)

    def play(self, request):
        id_midia = request.GET.get('id_midia')
        id_playout = request.GET.get('id_playout')
        playout = Playout.objects.get(id=id_playout)
        midia = Midia.objects.get(id=id_midia)
        playout.midia_atual = midia
        playout.save()
        response = self.client.send(PLAY(video_channel=1, clip=midia.nome_arquivo))
        return str(response)

    def pause_resume(self, request):
        if self.flag_pause_resume:
            response = self.client.send(PAUSE(video_channel=1))
            self.flag_pause_resume = not self.flag_pause_resume
        else:
            response = self.client.send(RESUME(video_channel=1))
            self.flag_pause_resume = not self.flag_pause_resume

        return str(response)

    def stop(self, request):
        response = self.client.send(STOP(video_channel=1))
        return str(response)

    def reconectar(self, request):
        self.client = Client()
        self.client.connect("localhost", 5250)

    def atualizar_ordem_payout(self, request):
        id = request.GET.get('id')
        ordem = request.GET.get('ordem')
        Midia_i.objects.filter(id=id).update(ordem=ordem)

    def carregar_tabela_playout(self, request):
        try:
            linhas = ""
            id_playout = request.GET.get('id_playout')
            playout = Playout.objects.get(id=id_playout)
            for midia in  Midia_i.objects.order_by("ordem").filter(playout=playout, ativo=True):
                print(self.client.send(CINF(filename=midia.midia.nome_arquivo)))
                linhas = linhas + "<tr id='{id}' data-id-midia='{id_midia}' class='clickableRow'>" \
                                    "<td> {titulo} </td>" \
                                    "<td> {duracao} </td>" \
                                  "</tr>".format(id=midia.id, id_midia=midia.midia.id, duracao=midia.midia.duracao, titulo=midia.midia.titulo)
            return {'linhas': linhas, 'id_midia_atual': playout.midia_atual.id}
        except Exception as e:
            print(e)
            print("Problemas ao montar Playout")

    def listar_arquivos_servidor(self, request):
        lista_arquivos = []
        arquivos = str(self.client.send(CLS())).split('200(CLS)')[1].split(',')
        for arquivo in arquivos:
            if arquivo.find('MOVIE') != -1:
                lista_arquivos.append(arquivo[arquivo.find('"') + 1:arquivo.find('" ')])
        return lista_arquivos