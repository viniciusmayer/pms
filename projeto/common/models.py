from django.contrib.auth.models import User
from django.db import models

class CommonInfo(models.Model):
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    # arquivado = models.BooleanField(default = True)
    data_hora_criacao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True, editable=False, blank=True)
    observacoes = models.CharField(null=True, blank=True, max_length=255)
    
    usuario = models.ForeignKey(User)
    
    class Meta:
        abstract = True
        ordering = ['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def ___unicode__(self):
        return self.nome
    
    def __str__(self):
        return self.nome

    def delete(self, using=None):
        self.excluido = True
        self.ativo = False
        models.Model.save(self, using=using)