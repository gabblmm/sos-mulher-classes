"Alunas:Anna Lilian, Anna Sophia, Gabrielly, Geovanna, Yasmin"
"Turma: 2 ano B informática"
import sys
class Excecaolocalizacaoigual(Exception):
    pass
class localizacao:
# Relação de associação simples com as classes tornozeleira, viatura e vitima
    def __init__(self, coordenadas, rua, bairro, numero, datahora):
        self.coordenadas = coordenadas
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.datahora = datahora

    def getcoordenadas(self):
        return self.coordenadas

    # Relação de agregacao com a classe botaoEmergencia, com localizacao sendo a parte do todo
    def atualizar_localizacao(self, nova_coordenada, nova_rua, novo_bairro, novo_numero, nova_datahora):
        try:
            if nova_coordenada == self.coordenadas:
                raise Excecaolocalizacaoigual
        except Excecaolocalizacaoigual:
            print("A localização não foi atualizada. A coordenada é a mesma.")
            return False
        else:
            self.coordenadas = nova_coordenada
            self.rua = nova_rua
            self.bairro = novo_bairro
            self.numero = novo_numero
            self.datahora = nova_datahora
            return True

from abc import ABC

class ExecaoSenhaIgual(Exception):
    pass
class ExecaoErroAutenticacao(Exception):
    pass
class ExcecaoCPFerrado(Exception):
    pass
class ExcecaoSenhaErrada(Exception):
    pass

class usuario(ABC):
#classe abstrata de operador e vitima, relação de herança
    #construtor
    def __init__(self,nome, cpf, senha):
    #atributos
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
    #metodos

    def fazer_login(self):
        try:
            cadastrousuario = input("informe o CPF:")
            if cadastrousuario != self.cpf:
                raise ExcecaoCPFerrado
        except ExcecaoCPFerrado:
            while cadastrousuario != self.cpf:
                cadastrousuario = input("CPF incorreto. Tente novamente: ")
        try:
            senhausuario = input("informe a senha: ")
            if senhausuario != self.senha:
                raise ExcecaoSenhaErrada
        except ExcecaoSenhaErrada:
            while senhausuario != self.senha:
                senhausuario = input("Senha incorreta. Tente novamente: ")        
        

    def atualizar_login(self):
        try: 
            nova_senha = input("informe a nova senha: ")
            if nova_senha == self.senha:
                raise ExecaoSenhaIgual    
        except ExecaoSenhaIgual:
            while nova_senha == self.senha:
                nova_senha = input("A nova senha é igual a senha atual! Escolha uma nova senha:")

        self.senha = nova_senha

    def recuperar_acesso(self):
        try:
            cpf_recuperar = input("Informe o CPF para recuperação de acesso: ")
            if cpf_recuperar != self.cpf:
                raise ExecaoErroAutenticacao
        except ExecaoErroAutenticacao:
            print("CPF não encontrado. Tente novamente.")
            return False
        else:
            print("Acesso recuperado com sucesso!")
            return True
       
class Excecaodiferente1(Exception):
    pass
class Excecaolocalizacaonegada(Exception):
    pass
class vitima(usuario):
    #relação de herança com classe usuario
    def __init__(self,nome,cpf,senha,numeroMPU, DadosAgressor, Cep):
        super().__init__(nome, cpf, senha)
        self.numeroMPU = numeroMPU
        self.DadosAgressor = DadosAgressor
        self.Cep = Cep

        #RELAÇÃO UML: Vitima 1 - 1..* Localizacao
        #Uma vítima pode possuir várias localizações.
        self.localizacoes = []

    def fazer_login(self):
        #relação de herança com a classe usuario
        return super().fazer_login()
    
    def atualizar_login(self):
        #relação de herança com a classe usuario
        return super().atualizar_login()

    #RELAÇÃO UML: Vitima ---- Localizacao
    def adicionar_localizacao(self, localizacao):
        self.localizacoes.append(localizacao)

    def ocultar_aplicativo(self):
        resposta = input("Deseja ocultar o aplicativo? (sim/não): ")
        if resposta == "sim":
            print("O aplicativo foi ocultado.")
        else:
            print("O aplicativo não foi ocultado.")


    def permitir_localizacao(self):
        try:
            permissao = input("Deseja permitir o acesso à localização? (sim/não): ")
            if permissao != "sim":
                raise Excecaolocalizacaonegada
            else:
                print("Acesso à localização permitido.")

        except Excecaolocalizacaonegada:
            while permissao != "sim":
                permissao = input("Para utilizar o aplicativo, é necessário permitir o acesso à localização. Deseja permitir? (sim/não): ")
            print("Acesso à localização permitido.")

    def acionar_sos_sos():
        #Relação de associação simples com a classe botaoEmergencia
        print("1 -> Acionar botão de SOS")
        try:
            botao_sos = input("Pressione 1 para acionar o SOS: ")
            if botao_sos != "1":
                raise Excecaodiferente1
            else:
                print("Botão de SOS ativado. A polícia já foi acionada.")
        except Excecaodiferente1:
            botao_sos = input("Deseja acionar o botão? Digite s para sim e n para não: ")
            if botao_sos == 's' or botao_sos == 'sim' or botao_sos == 'S':
                print("Botão de SOS ativado. A polícia já foi acionada.")
            else:
                print("Botão de emergência não acionado")
                sys.exit()
       
#RELAÇÃO UML:
#Agressor possui agregação com Tornozeleira
#Agressor possui associação com Localizacao
class agressor:

    def __init__(self,nome,cpf , tornozeleira, localizacao):
        self.nome = nome
        self.cpf = cpf
        #a relação de agregação está ocorrendo aqui
        self.tornozeleira = tornozeleira
        self.localizacao = localizacao
        
    def getnome(self):
        return self.nome

    def getcpf(self):
        return self.cpf

    def getlocalizacao(self):
        return self.localizacao.getcoordenadas()

class tornozeleira:
#associação simples com localização e estabelece uma relação de agregação com a classe agressor, sendo tornozeleira a parte do todo
    def __init__(self, coordenadas, rua, bairro, numero, datahora):
        self.coordenadas = coordenadas
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.datahora = datahora

    def getcoordenadas(self):
        return self.coordenadas

    def atualizar_localizacao(self, nova_coordenada, nova_rua, novo_bairro, novo_numero, nova_datahora):
        try:
            if nova_coordenada == self.coordenadas:
                raise Excecaolocalizacaoigual
            else:
                self.coordenadas = nova_coordenada
                self.rua = nova_rua
                self.bairro = novo_bairro
                self.numero = novo_numero
                self.datahora = nova_datahora
        except Excecaolocalizacaoigual:
            print("A localização não foi atualizada. A coordenada é a mesma.")       
      
    def emitir_alerta(self):
        coordenadas = self.getcoordenadas()
    
#RELAÇÃO UML: HERANÇA
#Operador herda de Usuário
class operador(usuario):

    def __init__(self, nome, cpf, senha, postoOperador):
        super().__init__(nome, cpf, senha)
        self.postoOperador = postoOperador

    def fazer_login(self):
        return super().fazer_login()

    def atualizar_login(self):
        return super().atualizar_login()

    def realizar_autenticacao(self, cadastrousuario, senhausuario):
        return super().realizar_autenticacao(cadastrousuario, senhausuario)

    def recuperar_acesso(self):
        return super().recuperar_acesso()

    def cadastrar_usuario(self, vitima):
        print("Vítima cadastrada com sucesso!")
        print("Nome:", vitima.nome)
        print("CPF:", vitima.cpf)
        print("Número da MPU:", vitima.numeroMPU)
        return vitima

    def dados_Agressor(self, agressor):
        print("Nome:", agressor.nome)
        print("CPF:", agressor.cpf)
        print("Tornozeleira:", agressor.tornozeleira)
        print("Localização:", agressor.localizacao.getcoordenadas())

    def receber_alerta(self, alerta):
        print("Alerta recebido pelo operador:", alerta)

    def localizar_vitima(self, localizacao):
        coordenadas = localizacao.getcoordenadas()
        print("Localização da vítima:", coordenadas)

    def localizar_agressor(self, localizacao):
        coordenadas = localizacao.getcoordenadas()
        print("Localização do agressor:", coordenadas)

class ExecaoMedidaInativa(Exception):
    pass

class mpu:
    def __init__(self, NumeroMPU, DadosVitima, DadosAgressor, distanciaMinima, dateRegistro, statusMedida):
    #relação de agregação com a classe vítima, sendo MPU a parte do todo.
        self.NumeroMPU = NumeroMPU
        self.DadosVitima = DadosVitima
        #RELAÇÃO composição: MPU - Vitima
        self.DadosAgressor = DadosAgressor
        #RELAÇÃO associação: MPU - Agressor
        self.distanciaMinima = distanciaMinima
        self.dateRegistro = dateRegistro
        self.statusMedida = statusMedida

    def getstatusMedida(self):
        try:
            if self.statusMedida != "ativa":
                raise ExecaoMedidaInativa
        except ExecaoMedidaInativa:
            sys.exit("Erro:O aplicativo não pode ser usado sem medida protetiva ativa. Entre em contato com a polícia para mais informações.")
        return self.statusMedida

    def setstatusMedida(self, novo_status):
        try:
            if novo_status != "ativa":
                raise ExecaoMedidaInativa
            else:
                self.statusMedida = novo_status

        except ExecaoMedidaInativa:
            sys.exit("Erro: O aplicativo não pode ser usado sem medida protetiva ativa. Entre em contato com a polícia para mais informações.")

        return self.statusMedida

    def getNumeroprocesso(self):
        return self.NumeroMPU

    def consultarMPU(self):
        #relação de agregação com a classe vítima, sendo MPU a parte do todo.
        print("Número do processo:", self.NumeroMPU)
        print("Dados da vitima:", self.DadosVitima.nome)
        print("Dados do agressor:", self.DadosAgressor.nome)
        print("Distancia minima:", self.distanciaMinima)
        print("Data do registro:", self.dateRegistro)
        print("Status da medida:", self.statusMedida)

class botao_emergencia:
    def __init__(self, localizacao, notificacao, horario):
        self.localizacao = localizacao
        self.notificacao = notificacao
        self.horario = horario

     #Relação de associação simples  com a classe vitima
    def emitir_alerta(self):
        print("o alerta foi emitido para o operador responsável.", self.notificacao, "no horário:", self.horario)

    #Relação de agregação com a classe localizacao
    def enviar_localizacao(self):
        coordenadas = self.localizacao.getcoordenadas()
        print("Localização enviada:", coordenadas)

class ExecaoStatusInvalido(Exception):
    pass
class ocorrencia:
    def __init__(self, datehora, status, dadosvitima, dadosagressor, localizacao):
        self.datehora = datehora
        self.status = status
        self.dadosvitima = dadosvitima
        self.dadosagressor = dadosagressor
        self.localizacao = localizacao

    def registros_ocorrencia(self):
        print("Ocorrência registrada:")
        print("Data e hora:", self.datehora)
        print("Status:", self.status)
        print("Dados da vítima:", self.dadosvitima.nome)
        print("Dados do agressor:", self.dadosagressor.nome)
        print("Localização:", self.localizacao.getcoordenadas())

    def atualizar_status(self, novo_status):
        try:
            if novo_status not in ["em andamento", "finalizada"] or self.status == "finalizada" and novo_status != "finalizada":
                raise ExecaoStatusInvalido
            else:
                self.status = novo_status
                print("Status da ocorrência atualizado para:", self.status)

        except ExecaoStatusInvalido:
            print("Erro: Status inválido.")

    # Relação de associação simples com a classe operador e relação de agregação com a classe viatura, sendo ocorrencia a parte do todo
    def encaminhar_ocorrencia(self, operador):
        try:
            if self.status != "em andamento":
                raise ExecaoStatusInvalido
            print("Encaminhando ocorrência para o operador:", operador)
        except ExecaoStatusInvalido:
            print("A ocorrência não pode ser encaminhada nesse status.")

class viatura:

    def __init__(self, policial, placa, localizacao):
        self.policial = policial
        self.placa = placa
        self.localizacao = localizacao

    #Relação de agregação com a classe ocorrencia, com viatura sendo o todo
    def receber_ocorrencia(self, ocorrencias):
        ocorrencias.registros_ocorrencia()

    #Relação de associação simples coma a classe localizacao
    def atualizar_localizacao(self, nova_coordenada, nova_rua, novo_bairro, novo_numero, nova_datahora):
        atualizou = self.localizacao.atualizar_localizacao(nova_coordenada, nova_rua, novo_bairro, novo_numero, nova_datahora)

        if atualizou:
            print("Localização da viatura em tempo real:", self.localizacao.getcoordenadas())
    def  finalizar_ocorrencia(self, ocorrencia):
        if ocorrencia.status == "finalizada":
            print("A ocorrência já está finalizada.")
        else:
            ocorrencia.status = "finalizada"
            print("Ocorrência finalizada pelo policial.")