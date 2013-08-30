from django import forms
from projeto.models import Area, Artefato, Pessoa, Tipo, Status, Configuracao, \
    Equipe, Fato, Iteracao, AcompanhamentoIteracao, Item, Projeto

class StatusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Status

class ArtefatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArtefatoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Artefato

class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Tipo

class AreaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Area

class PessoaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Pessoa

class ConfiguracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfiguracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Configuracao

class IteracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IteracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Iteracao
        
class AcompanhamentoIteracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AcompanhamentoIteracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = AcompanhamentoIteracao
        
class EquipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipeForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()

    class Meta:
        model = Equipe
    
class FatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FatoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Fato

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Item

class ProjetoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjetoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Projeto
