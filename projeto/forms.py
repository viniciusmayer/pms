from django import forms

from projeto.models import Status, Artefato, Tipo, Area, Pessoa, Configuracao, \
    Iteracao, AcompanhamentoIteracao, Equipe, Fato, Item, Projeto


class StatusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Status
        exclude = []

class ArtefatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArtefatoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Artefato
        exclude = []

class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Tipo
        exclude = []

class AreaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Area
        exclude = []

class PessoaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Pessoa
        exclude = []

class ConfiguracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfiguracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Configuracao
        exclude = []

class IteracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IteracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Iteracao
        exclude = []
        
class AcompanhamentoIteracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AcompanhamentoIteracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = AcompanhamentoIteracao
        exclude = []
        
class EquipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipeForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()

    class Meta:
        model = Equipe
        exclude = []
    
class FatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FatoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Fato
        exclude = []

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Item
        exclude = []

class ProjetoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjetoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Projeto
        exclude = []