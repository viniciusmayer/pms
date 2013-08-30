from datetime import datetime, timedelta
from django.contrib.auth.models import User
from projeto.models import IteracaoPessoa, Area, Pessoa, Projeto, Configuracao, \
    Iteracao, Fato, FatoPessoa, Tipo
import uuid

class TipoBuilder():
    @staticmethod
    def create(nome, categoria):
        return Tipo.objects.create(nome=nome,
                                   categoria=categoria,
                                   usuario=UsuarioBuilder.sessionUser())

class FatoPessoaBuilder():
    @staticmethod
    def create(fato, pessoa):
        return FatoPessoa.objects.create(fato=fato, pessoa=pessoa)

'''
CATEGORIA = (
    ('IT', 'Item'),
    ('FA', 'Fato'),
)
'''
class FatoBuilder():
    @staticmethod
    def create(nome, ocorrencias, tempo, numeroPessoas, categoria):
        fato = Fato.objects.create(nome=nome,
                                   tempo=tempo,
                                   ocorrencias=ocorrencias,
                                   iteracao=IteracaoBuilder.create(UUIDGenerator.uuid()),
                                   tipo=TipoBuilder.create(UUIDGenerator.uuid(), categoria),
                                   usuario=UsuarioBuilder.sessionUser(),)
        
        for i in range(numeroPessoas):
            pessoa = PessoaBuilder.create(UUIDGenerator.uuid())
            FatoPessoaBuilder.create(fato, pessoa)
        
        return fato

class AreaBuilder():
    @staticmethod
    def create(nome):
        return Area.objects.create(nome=nome,
                                   responsavel=PessoaBuilder.create(UUIDGenerator.uuid()),
                                   usuario=UsuarioBuilder.sessionUser(),)

class UsuarioBuilder():
    usuario = None  # usarei o mesmo usuario para execucao de todos os testes
    @staticmethod
    def sessionUser():
        if UsuarioBuilder.usuario is None:
            UsuarioBuilder.usuario = User.objects.create(username='usuario_teste',
                                                         password='password',)
        return UsuarioBuilder.usuario

    @staticmethod
    def create(username, first_name='', last_name='', email=''):
        return User.objects.create(username=username,
                                   password='password',
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)
    
class ProjetoBuilder():
    @staticmethod
    def create(nome):
        return Projeto.objects.create(nome=nome,
                                      responsavel=PessoaBuilder.create(UUIDGenerator.uuid()),
                                      demandante=AreaBuilder.create(UUIDGenerator.uuid()),
                                      demandada=AreaBuilder.create(UUIDGenerator.uuid()),
                                      usuario=UsuarioBuilder.sessionUser(),)

class PessoaBuilder():
    @staticmethod
    def create(username, first_name='', last_name='', email=''):
        return Pessoa.objects.create(user=UsuarioBuilder.create(username, first_name, last_name, email),
                                     area=AreaBuilder.create(UUIDGenerator.uuid()),
                                     usuario=UsuarioBuilder.sessionUser(),)

class IteracaoPessoaBuilder():
    @staticmethod
    def create(iteracao, pessoa):
        return IteracaoPessoa.objects.create(iteracao=iteracao,
                                             pessoa=pessoa,)
    
class ConfiguracaoBuilder():
    @staticmethod
    def create_HorasPorDia(horasPorDia):
        c = Configuracao.objects.filter(chave='HORAS_POR_DIA')
        c.delete()
        Configuracao.objects.create(nome='configuracao_horas_por_dia',
                                    chave='HORAS_POR_DIA',
                                    valor=horasPorDia,
                                    usuario=UsuarioBuilder.sessionUser(),)

class IteracaoBuilder():
    @staticmethod
    def create(nome, numeroDeDias=0, numeroDeDiasNaoUteis=0, numeroPessoas=0):
        data_inicio = datetime.now()
        data_fim = data_inicio + timedelta(days=numeroDeDias)
        iteracao = Iteracao.objects.create(nome=nome,
                                           data_inicio=data_inicio,
                                           data_fim=data_fim,
                                           numero_dias_nao_uteis=numeroDeDiasNaoUteis,
                                           projeto=ProjetoBuilder.create(UUIDGenerator.uuid()),
                                           usuario=UsuarioBuilder.sessionUser(),)

        for i in range(numeroPessoas):
            pessoa = PessoaBuilder.create(UUIDGenerator.uuid())
            IteracaoPessoaBuilder.create(iteracao, pessoa)
            
        return iteracao
    
class UUIDGenerator():
    @staticmethod
    def uuid():
        return str(uuid.uuid4())[:29]
