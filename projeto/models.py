from datetime import datetime, timedelta
from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models

from common.models import CommonInfo


class Status(CommonInfo):
    predecessora = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        verbose_name_plural = 'status'

class Artefato(CommonInfo):
    pass

class Tipo(CommonInfo):
    CATEGORIA = (
        ('IT', 'Item'),
        ('FA', 'Fato'),
        ('RE', 'Relacao'),
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIA)

class Area(CommonInfo):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})

class Pessoa(models.Model):
    excluido = models.BooleanField(default=False)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)
    observacoes = models.CharField(null=True, blank=True, max_length=255)

    user = models.ForeignKey(User, unique=True, related_name='profile')
    area = models.ManyToManyField(Area, through='AreaPessoa')
    usuario = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-user__is_active', 'user__username', 'user__first_name', 'user__last_name', 'user__email', 'observacoes', '-data_hora_atualizacao', '-user__date_joined']
        
    def ___unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username
    
    '''
    pega o username e, alem disso, tenta incluir entre
    parenteses depois do username o nome completo (first + last name).
    senao, se nao tiver o nome completo, inclui o email
    '''
    def nome(self):
        nome = self.username()
        first_name = self.first_name()
        last_name = self.last_name()
        email = self.email()
        fullname = None
        if first_name is not None and first_name:
            fullname = first_name
            if last_name is not None and last_name:
                fullname += ' '
                fullname += last_name
            else:
                fullname = None
        if fullname is not None and fullname:
            nome += ' ('
            nome += fullname
            nome += ')'
        elif email is not None and email:
            nome += ' ('
            nome += email
            nome += ')'
        return nome
    nome.short_description = 'Name'
        
    def username(self):
        return self.user.username
    username.short_description = 'Username'
    
    def first_name(self):
        return self.user.first_name
    first_name.short_description = 'First Name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'Last Name'

    def email(self):
        return self.user.email
    email.short_description = 'E-mail'

    def is_active(self):
        return self.user.is_active
    is_active.short_description = 'Ativo'
    is_active.boolean = True

    def date_joined(self):
        return self.user.date_joined
    date_joined.short_description = 'Date Joined'
    
    def delete(self, using=None):
        self.excluido = True
        self.ativo = False
        models.Model.save(self, using=using)

class AreaPessoa(models.Model):
    area = models.ForeignKey(Area, limit_choices_to={'ativo':True, 'excluido':False})
    pessoa = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'RE'})

class Configuracao(CommonInfo):
    chave = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'configuracoes'

class Projeto(CommonInfo):
    responsavel = models.ForeignKey('Pessoa', limit_choices_to={'user__is_active':True, 'excluido':False})
    demandante = models.ForeignKey(Area, limit_choices_to={'ativo':True, 'excluido':False}, related_name='area_demandante_projeto')
    demandada = models.ForeignKey(Area, limit_choices_to={'ativo':True, 'excluido':False}, related_name='area_demandada_projeto')

    # TODO refatorar
    # FIXME testar
    def total_pontos(self):
        total_pontos = None
        iters = self.iteracao_set.all()
        for _iter in iters:
            acom_iters = _iter.acompanhamentoiteracao_set.all()
            for acom_iter in acom_iters:
                realizado = acom_iter.realizado
                if realizado is not None:
                    if realizado > 0: #FIXME SMELL
                        if total_pontos is None:
                            total_pontos = 0
                        total_pontos += realizado
        return total_pontos
    total_pontos.short_description = 'Total Pontos'
    
    # TODO refatorar
    # FIXME testar
    def total_horas(self):
        zero = timedelta()
        hora_acum = timedelta()
        iters = self.iteracao_set.all()
        for _iter in iters:
            # horas reais da iteracao mesmo?
            hora_pont = _iter.horas_reais()
            if hora_pont is not None:
                if hora_pont > zero:
                    hora_acum += hora_pont
        return hora_acum
    total_horas.short_description = 'Total Horas'
    
    # TODO refatorar
    # FIXME testar
    def horas_por_ponto(self):
        zero = timedelta()
        hora_acum = timedelta()
        nume_iter = 0
        iters = self.iteracao_set.all()
        for _iter in iters:
            acom_iters = _iter.acompanhamentoiteracao_set.all()
            for acom_iter in acom_iters:
                hora_pont = acom_iter.horas_por_ponto()
                if hora_pont is not None:
                    if hora_pont > zero:
                        nume_iter += 1
                        hora_acum += hora_pont
        if nume_iter > 0:
            if  hora_acum > zero:
                # FIXME formatar a data para apresentacao
                return hora_acum / nume_iter
    horas_por_ponto.short_description = 'Horas por ponto'

    # TODO refatorar
    # FIXME testar
    def indice(self):
        acum_tax = 0.0
        nume_acom_iter = 0;
        iters = self.iteracao_set.all()
        for _iter in iters:
            acom_iters = _iter.acompanhamentoiteracao_set.all()
            for acom_iter in acom_iters:
                real = acom_iter.realizado
                if real is not None:
                    nume_acom_iter += 1
                    tax = acom_iter.taxa()
                    if tax is not None:
                        acum_tax += tax
        if nume_acom_iter > 0:
            return round(acum_tax / nume_acom_iter, 2)
    indice.short_description = 'Indice'

class Iteracao(CommonInfo):
    data_inicio = models.DateField(default=datetime.now())
    data_fim = models.DateField(default=datetime.now() + timedelta(days=12))
    numero_dias_nao_uteis = models.PositiveIntegerField(default=5, help_text='primeira segunda-feira, ultima sexta-feira, sabado, domingo, terca-feira pela manha e quinta-feira pela tarde')
    
    predecessora = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    pessoas = models.ManyToManyField(Pessoa, through='IteracaoPessoa')
    projeto = models.ForeignKey(Projeto, limit_choices_to={'ativo':True, 'excluido':False})

    class Meta:
        verbose_name_plural = 'Iteracoes'

    # TODO refatorar
    # FIXME testar
    def horas_reais(self):
        hora_reai = self.horas_timedelta()
        hora_fato = self.horas_fatos()
        if hora_fato is not None:
            hora_reai = hora_reai - hora_fato  
        # FIXME formatar a data para apresentacao
        return hora_reai
    horas_reais.short_description = 'Horas reais'
    
    # TODO refatorar
    def horas_fatos(self):
        hora_fato = timedelta()
        fatos = self.fato_set.all()
        for fato in fatos:
            tota_hora = fato.total_horas()
            if tota_hora is not None:
                hora_fato = hora_fato + tota_hora
        # FIXME formatar a data para apresentacao
        return hora_fato
    horas_fatos.short_description = 'Horas fatos'
    
    # TODO refatorar
    def horas_timedelta(self):
        # FIXME formatar a data para apresentacao
        return timedelta(hours=self.horas())
    horas_timedelta.short_description = 'Horas'
    
    # TODO refatorar
    def horas(self):
        dias = (self.data_fim - self.data_inicio).days
        dias -= self.numero_dias_nao_uteis
        if dias < 0:  # FIXME SMELL
            dias = 0
        nume_pess = self.pessoas.count()
        hora_dia = int(Configuracao.objects.get(chave__exact='HORAS_POR_DIA').valor)
        return nume_pess * hora_dia * dias

class IteracaoPessoa(models.Model):
    data_hora_inicio = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True, editable=False)

    iteracao = models.ForeignKey(Iteracao, limit_choices_to={'ativo':True, 'excluido':False})
    pessoa = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})

class AcompanhamentoIteracao(models.Model):
    ativo = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    data_hora_criacao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True, editable=False, blank=True)
    observacoes = models.CharField(null=True, blank=True, max_length=255)

    objetivo = models.DecimalField(max_digits=5, decimal_places=2)
    real = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    realizado = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    mc = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})
    iteracao = models.ForeignKey(Iteracao, limit_choices_to={'ativo':True, 'excluido':False})
    usuario = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-ativo', 'iteracao__nome', 'mc__user__username', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'acompanhamento iteracoes'
        
    def ___unicode__(self):
        return self.iteracao.nome
    
    def __str__(self):
        return self.iteracao.nome
    
    def nome_iteracao(self):
        return self.iteracao.nome
    nome_iteracao.short_description = 'Iteracao'

    def nome_mc(self):
        return self.mc.nome()
    mc.short_description = 'MC'
    
    # TODO refatorar
    # FIXME testar
    def taxa(self):
        if self.realizado is not None:
            var1 = self.realizado * Decimal(0.1)
            var2 = var1 / self.real
            var3 = var2 * 10
            return round(var3, 2)
    taxa.short_description = 'Taxa'

    # TODO refatorar
    # FIXME testar
    def horas_por_ponto(self):
        hora_iter = self.iteracao.horas()
        pont_real = self.realizado
        if pont_real is not None: 
            hora_pont = hora_iter / pont_real
            hora = int(hora_pont)
            minu = int((hora_pont - hora) * 60)
            # FIXME formatar a data para apresentacao
            return timedelta(hours=hora, minutes=minu)
    horas_por_ponto.short_description = 'Horas por ponto'
    
    def delete(self, using=None):
        self.excluido = True
        self.ativo = False
        models.Model.save(self, using=using)

class Equipe(CommonInfo):
    pessoas = models.ManyToManyField(Pessoa, through='EquipePessoa')
    
    def usernames(self):
        return ', '.join([p.user.username for p in self.pessoas.all()])
    usernames.short_description = 'Pessoas'
    
class EquipePessoa(models.Model):
    data_hora_inicio = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True, editable=False)
    
    equipe = models.ForeignKey(Equipe, limit_choices_to={'ativo':True, 'excluido':False})
    pessoa = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})
    
class Fato(CommonInfo):
    data = models.DateField(default=datetime.now())
    ocorrencias = models.PositiveIntegerField(default='1')
    
    # TODO qual eh o tipo de dado mais adequado para este caso (timedelta)
    tempo = models.CharField(help_text='hhh:mm:ss', max_length=10, default='1:00:00')
    
    iteracao = models.ForeignKey(Iteracao, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'FA'})
    pessoas = models.ManyToManyField(Pessoa, through='FatoPessoa')

    # TODO refatorar
    def total_horas(self):
        tota_hora = self.tempo_horas() * self.numero_pessoas() * self.ocorrencias
        # FIXME formatar a data para apresentacao
        return tota_hora
    total_horas.short_description = 'Total Horas'

    # TODO refatorar
    # FIXME testar? sim!
    def tempo_horas(self):
        partes = str(self.tempo).split(':')
        horas = int(partes[0])
        minutos = int(partes[1])
        segundos = int(partes[2])
        return timedelta(hours=horas, minutes=minutos, seconds=segundos)
    tempo_horas.short_description = 'Tempo'
    
    # TODO refatorar?
    def numero_pessoas(self):
        return self.pessoas.count()
    numero_pessoas.short_description = 'Pessoas'

class FatoPessoa(models.Model):
    data_hora_inicio = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True, editable=False)
    
    fato = models.ForeignKey(Fato, limit_choices_to={'ativo':True, 'excluido':False})
    pessoa = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})

class Item(CommonInfo):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    artefato = models.ForeignKey(Artefato, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'IT'})
    responsavel = models.ForeignKey(Pessoa, limit_choices_to={'user__is_active':True, 'excluido':False})
    demandante = models.ForeignKey(Area, limit_choices_to={'ativo':True, 'excluido':False}, related_name='area_demandante_item')
    demandada = models.ForeignKey(Area, limit_choices_to={'ativo':True, 'excluido':False}, related_name='area_demandada_item')
    
    iteracao = models.ForeignKey(Iteracao, null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    andamentos = models.ManyToManyField(Status, through='Andamento')

    class Meta:
        verbose_name_plural = 'itens'
        
class Andamento(CommonInfo):
    data_hora_inicio = models.DateTimeField(auto_now_add=True)
    data_hora_fim = models.DateTimeField()

    item = models.ForeignKey(Item)
    status = models.ForeignKey(Status)