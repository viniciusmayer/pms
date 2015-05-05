from django.contrib import admin

from projeto.forms import StatusForm, ArtefatoForm, TipoForm, AreaForm, \
    PessoaForm, ConfiguracaoForm, IteracaoForm, AcompanhamentoIteracaoForm, \
    EquipeForm, FatoForm, ItemForm, ProjetoForm
from projeto.models import Tipo, Area, AreaPessoa, Pessoa, Configuracao, \
    IteracaoPessoa, Iteracao, AcompanhamentoIteracao, EquipePessoa, FatoPessoa, \
    Fato, Projeto


class StatusAdmin(admin.ModelAdmin):
    form = StatusForm
    list_display = ['nome', 'observacoes', 'predecessora', 'ativo']
    list_filter = ['data_hora_atualizacao', 'predecessora']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(StatusAdmin, self).queryset(request)
        return qs.filter(excluido=False)
    
#admin.site.register(Status, StatusAdmin)

class ArtefatoAdmin(admin.ModelAdmin):
    form = ArtefatoForm
    list_display = ['nome', 'observacoes', 'ativo']
    list_filter = ['data_hora_atualizacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(ArtefatoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

# admin.site.register(Artefato, ArtefatoAdmin)

class TipoAdmin(admin.ModelAdmin):
    form = TipoForm
    list_display = ['nome', 'categoria', 'observacoes', 'ativo']
    list_filter = ['data_hora_atualizacao', 'categoria']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(TipoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Tipo, TipoAdmin)

class AreaAdmin(admin.ModelAdmin):
    form = AreaForm
    list_display = ['nome', 'parent', 'observacoes', 'ativo']
    list_filter = ['parent', 'data_hora_atualizacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(AreaAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Area, AreaAdmin)

class AreaPessoaAdmin(admin.TabularInline):
    model = AreaPessoa
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    form = PessoaForm
    list_display = ['username', 'first_name', 'last_name', 'email', 'nome', 'observacoes', 'is_active']
    list_filter = ['data_hora_atualizacao', 'area']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'observacoes']
    # date_hierarchy = 'date_joined'
    exclude = ['usuario', 'excluido']
    inlines = (AreaPessoaAdmin,)
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(PessoaAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Pessoa, PessoaAdmin)

class ConfiguracaoAdmin(admin.ModelAdmin):
    form = ConfiguracaoForm
    list_display = ['nome', 'chave', 'valor', 'observacoes', 'ativo']
    list_filter = ['data_hora_atualizacao']
    search_fields = ['nome', 'chave', 'valor', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(ConfiguracaoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Configuracao, ConfiguracaoAdmin)
   
class IteracaoPessoaAdmin(admin.TabularInline):
    model = IteracaoPessoa

class IteracaoAdmin(admin.ModelAdmin):
    form = IteracaoForm
    list_display = ['nome', 'data_inicio', 'data_fim', 'horas_timedelta', 'horas_fatos', 'horas_reais', 'projeto', 'predecessora', 'observacoes', 'ativo']
    list_filter = ['projeto', 'data_inicio', 'data_fim']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_inicio'
    exclude = ['usuario', 'excluido']
    inlines = (IteracaoPessoaAdmin,)
     
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(IteracaoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Iteracao, IteracaoAdmin)

class AcompanhamentoIteracaoAdmin(admin.ModelAdmin):
    form = AcompanhamentoIteracaoForm
    list_display = ['nome_iteracao', 'nome_mc', 'objetivo', 'real', 'realizado', 'taxa', 'horas_por_ponto', 'observacoes', 'ativo']
    list_filter = ['iteracao', 'mc']
    search_fields = ['mc__user__username', 'iteracao__nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(AcompanhamentoIteracaoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(AcompanhamentoIteracao, AcompanhamentoIteracaoAdmin)

class EquipePessoaAdmin(admin.TabularInline):
    model = EquipePessoa

class EquipeAdmin(admin.ModelAdmin):
    form = EquipeForm
    list_display = ['nome', 'usernames', 'observacoes', 'ativo']
    list_filter = ['data_hora_atualizacao', 'pessoas__user__username']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    inlines = (EquipePessoaAdmin,)
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(EquipeAdmin, self).queryset(request)
        return qs.filter(excluido=False)
    
# admin.site.register(Equipe, EquipeAdmin)

class FatoPessoaAdmin(admin.TabularInline):
    model = FatoPessoa
    
class FatoAdmin(admin.ModelAdmin):
    form = FatoForm
    list_display = ['nome', 'data', 'tempo_horas', 'ocorrencias', 'numero_pessoas', 'total_horas', 'tipo', 'iteracao', 'observacoes', 'ativo']
    list_filter = ['data_hora_atualizacao', 'tipo', 'iteracao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data'
    exclude = ['usuario', 'excluido']
    inlines = (FatoPessoaAdmin,)
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(FatoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Fato, FatoAdmin)

class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ['iteracao', 'demandante', 'parent', 'nome', 'artefato', 'tipo', 'responsavel', 'demandada', 'ativo']
    list_filter = ['iteracao', 'demandante', 'artefato', 'tipo', 'responsavel', 'demandada']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(ItemAdmin, self).queryset(request)
        return qs.filter(excluido=False)

# admin.site.register(Item, ItemAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    form = ProjetoForm
    list_display = ['nome', 'total_horas', 'total_pontos', 'horas_por_ponto', 'indice', 'responsavel', 'demandante', 'demandada', 'observacoes', 'ativo']
    list_filter = ['responsavel', 'demandante', 'demandada', 'data_hora_atualizacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(ProjetoAdmin, self).queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Projeto, ProjetoAdmin)