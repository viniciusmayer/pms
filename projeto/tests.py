from datetime import timedelta
from projeto.builders import ConfiguracaoBuilder, IteracaoBuilder, FatoBuilder, \
    PessoaBuilder
import unittest

'''
config: 7 | dia: 1 | naoUtil: 0 | pessoa: 1 | horas: 7
config: 7 | dia: 1 | naoUtil: 0 | pessoa: 3 | horas: 21
config: 7 | dia: 3 | naoUtil: 0 | pessoa: 1 | horas: 21
config: 7 | dia: 3 | naoUtil: 0 | pessoa: 3 | horas: 63
config: 7 | dia: 3 | naoUtil: 1 | pessoa: 1 | horas: 14
config: 7 | dia: 3 | naoUtil: 1 | pessoa: 3 | horas: 42
config: 7 | dia: 0 | naoUtil: 0 | pessoa: 0 | horas: 0
config: 7 | dia: 0 | naoUtil: 1 | pessoa: 1 | horas: 0
config: 7 | dia: 0 | naoUtil: 0 | pessoa: 1 | horas: 0
config: 7 | dia: 1 | naoUtil: 0 | pessoa: 0 | horas: 0
config: 7 | dia: 3 | naoUtil: 1 | pessoa: 0 | horas: 0
config: 7 | dia: 1 | naoUtil: 3 | pessoa: 1 | horas: 0
'''
class IteracaoTestCase_ConfiguracaoIgualA7(unittest.TestCase):
    def setUp(self):
        ConfiguracaoBuilder.create_HorasPorDia(7)

    def tearDown(self):
        pass
        
    def test_dias_1_nao_uteis_0_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_1_n_util_0_pess_1', 1, 0, 1)
        horas = iteracao.horas()
        valor = 7
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_1_nao_uteis_0_pessoas_3(self):
        iteracao = IteracaoBuilder.create('test_d_1_n_util_0_pess_3', 1, 0, 3)
        horas = iteracao.horas()
        valor = 21
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_0_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_0_pess_1', 3, 0, 1)
        horas = iteracao.horas()
        valor = 21
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_0_pessoas_3(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_0_pess_3', 3, 0, 3)
        horas = iteracao.horas()
        valor = 63
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_1_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_pess_1', 3, 1, 1)
        horas = iteracao.horas()
        valor = 14
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_1_pessoas_3(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_pess_3', 3, 1, 3)
        horas = iteracao.horas()
        valor = 42
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
    
    def test_dias_0_nao_uteis_0_pessoas_0(self):
        iteracao = IteracaoBuilder.create('test_d_0_n_util_0_pess_0')
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_0_nao_uteis_1_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_0_n_util_1_pess_1', 0, 1, 1)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_0_nao_uteis_0_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_0_n_util_0_pess_1', 0, 0, 1)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_1_nao_uteis_0_pessoas_0(self):
        iteracao = IteracaoBuilder.create('test_d_1_n_util_0_pess_0', 1, 0, 0)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_3_nao_uteis_1_pessoas_0(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_pess_0', 3, 1, 0)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_1_nao_uteis_3_pessoas_1(self):
        iteracao = IteracaoBuilder.create('test_d_1_n_util_3_pess_1', 1, 3, 1)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

'''
config: 0 | dia: 0 | naoUtil: 0 | pessoa: 0 | horas: 0
config: 0 | dia: 3 | naoUtil: 1 | pessoa: 3 | horas: 0
'''
class IteracaoTestCase_ConfiguracaoIgualA0(unittest.TestCase):  
    def setUp(self):
        ConfiguracaoBuilder.create_HorasPorDia(0)

    def tearDown(self):
        pass

    def test_dias_0_nao_uteis_0_pessoas_0(self):
        iteracao = IteracaoBuilder.create('test_d_0_n_util_0_pes_0_hr_0')
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_1_pessoas_3(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_pes_3_hr_0', 3, 1, 3)
        horas = iteracao.horas()
        valor = 0
        self.assertEqual(horas, valor, 'O numero de horas nao eh %s: %s' % (valor, horas))
        
    def test_dias_0_nao_uteis_0_pessoas_0_fatos_0(self):
        iteracao = IteracaoBuilder.create('test_d_0_n_util_0_p_0_f_0_hr_0')
        horas_fatos = iteracao.horas_fatos()
        valor = timedelta(hours=0, minutes=0, seconds=0)
        self.assertEqual(horas_fatos, valor, 'O numero de horas relativas a fatos nao eh %s: %s' % (valor, horas_fatos))

    def test_dias_3_nao_uteis_1_pessoas_3_fatos_0(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_p_3_f_0_hr_0', 3, 1, 3)
        horas = iteracao.horas_fatos()
        valor = timedelta(hours=0, minutes=0, seconds=0)
        self.assertEqual(horas, valor, 'O numero de horas relativas a fatos nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_1_pessoas_3_fatos_1(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_p_3_f_1_hr_0', 3, 1, 3, 1, 1, 1)
        horas = iteracao.horas_fatos()
        valor = timedelta(hours=3, minutes=0, seconds=0)
        self.assertEqual(horas, valor, 'O numero de horas relativas a fatos nao eh %s: %s' % (valor, horas))

    def test_dias_3_nao_uteis_1_pessoas_3_fatos_3(self):
        iteracao = IteracaoBuilder.create('test_d_3_n_util_1_p_3_f_1_hr_0', 3, 1, 3, 3, 2, 2)
        horas = iteracao.horas_fatos()
        valor = timedelta(hours=36, minutes=0, seconds=0)
        self.assertEqual(horas, valor, 'O numero de horas relativas a fatos nao eh %s: %s' % (valor, horas))
        
class FatoTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_tempo_horas(self):
        fato = FatoBuilder.create('testTempoEmHoras_o_0_t_12345_n_0', 0, '1:23:45', 0, 'FA')
        temp_hora = fato.tempo_horas()
        tempo = timedelta(hours=1, minutes=23, seconds=45)
        self.assertEqual(temp_hora, tempo, 'O tempo em horas nao eh %s: %s' % (tempo, temp_hora))
        
    '''
    test_o_0_t_12345_p_1
    ocorrencia: 0 | tempo: 1:23:45 | pessoa: 1 | horas: 0:00:00
    test_o_1_t_0:00:00_p_1
    ocorrencia: 1 | tempo: 0:00:00 | pessoa: 1 | horas: 0:00:00
    test_o_1_t_12345_p_0
    ocorrencia: 1 | tempo: 1:23:45 | pessoa: 0 | horas: 0:00:00
    '''
    def test_ocorrencias_0_tempo_12345_pessoas_1(self):
        fato = FatoBuilder.create('test_o_0_t_12345_p_1', 0, '1:23:45', 1, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta()
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    def test_ocorrencias_1_tempo_00000_pessoas_1(self):
        fato = FatoBuilder.create('test_o_1_t_00000_p_1', 1, '0:00:00', 1, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta()
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    def test_ocorrencias_1_tempo_12345_pessoas_0(self):
        fato = FatoBuilder.create('test_o_1_t_12345_p_0', 1, '1:23:45', 0, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta()
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    '''
    test_o_1_t_12345_p_1
    ocorrencia: 1 | tempo: 1:23:45 | pessoa: 1 | horas: 1:23:45
    test_o_1_t_12345_p_3
    ocorrencia: 1 | tempo: 1:23:45 | pessoa: 3 | horas: 4:11:15
    test_o_3_t_12345_p_1
    ocorrencia: 3 | tempo: 1:23:45 | pessoa: 1 | horas: 4:11:15
    test_o_3_t_12345_p_3
    ocorrencia: 3 | tempo: 1:23:45 | pessoa: 3 | horas: 12:33:45
    '''
    def test_ocorrencias_1_tempo_12345_pessoas_1(self):
        fato = FatoBuilder.create('test_o_1_t_12345_p_1', 1, '1:23:45', 1, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta(hours=1, minutes=23, seconds=45)
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    def test_ocorrencias_1_tempo_12345_pessoas_3(self):
        fato = FatoBuilder.create('test_o_1_t_12345_p_3', 1, '1:23:45', 3, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta(hours=4, minutes=11, seconds=15)
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    def test_ocorrencias_3_tempo_12345_pessoas_1(self):
        fato = FatoBuilder.create('test_o_3_t_12345_p_1', 3, '1:23:45', 1, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta(hours=4, minutes=11, seconds=15)
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
    def test_ocorrencias_3_tempo_12345_pessoas_3(self):
        fato = FatoBuilder.create('test_o_3_t_12345_p_3', 3, '1:23:45', 3, 'FA')
        total_horas = fato.total_horas()
        tempo = timedelta(hours=12, minutes=33, seconds=45)
        self.assertEqual(total_horas, tempo, 'O total de horas nao eh %s: %s' % (tempo, total_horas))
        
class PessoaTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    '''
    pega o username e, alem disso, tenta incluir entre
    parenteses depois do username o nome completo (first + last name).
    senao, se nao tiver o nome completo, inclui o email
    '''
    def test_username(self):
        pessoa = PessoaBuilder.create('username')
        nome = pessoa.nome()
        valor = 'username'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))

    def test_username_fn(self):
        pessoa = PessoaBuilder.create('username_fn', 'fn')
        nome = pessoa.nome()
        valor = 'username_fn'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))
    
    def test_username_fn_ln(self):
        pessoa = PessoaBuilder.create('username_fn_ln', 'fn', 'ln')
        nome = pessoa.nome()
        valor = 'username_fn_ln (fn ln)'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))
    
    def test_username_fn_email(self):
        pessoa = PessoaBuilder.create('username_fn_email', 'fn', email='email')
        nome = pessoa.nome()
        valor = 'username_fn_email (email)'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))
    
    def test_username_fn_ln_email(self):
        pessoa = PessoaBuilder.create('username_fn_ln_email', 'fn', 'ln', 'email')
        nome = pessoa.nome()
        valor = 'username_fn_ln_email (fn ln)'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))
    
    def test_username_ln(self):
        pessoa = PessoaBuilder.create('username_ln', last_name='ln')
        nome = pessoa.nome()
        valor = 'username_ln'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))
    
    def test_username_ln_email(self):
        pessoa = PessoaBuilder.create('username_ln_email', last_name='ln', email='email')
        nome = pessoa.nome()
        valor = 'username_ln_email (email)'
        self.assertEqual(nome, valor, 'O nome nao eh %s: %s' % (valor, nome))