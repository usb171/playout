from django.db import models

class Playout(models.Model):
    ativo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=250, verbose_name='Título', blank=False, null=True)
    midia_atual = models.ForeignKey('Midia', verbose_name="Mídia Atual", on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Playout'
        verbose_name_plural = 'Playout'

    def __str__(self):
        return self.titulo


class Midia(models.Model):
    ativo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=250, verbose_name='Título', blank=False, null=True)
    duracao = models.CharField(max_length=20, verbose_name='Duração', blank=False, null=True)
    nome_arquivo = models.CharField(max_length=200, verbose_name='Nome arquivo', blank=False, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'

    def __str__(self):
        return self.titulo


class Midia_i(models.Model):
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(null=True, default=1)
    midia = models.ForeignKey('Midia', on_delete=models.CASCADE, null=True, blank=False)
    playout = models.ForeignKey('Playout', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'

    def __str__(self):
        return self.midia.titulo