"Alunas:Anna Lilian, Anna Sophia, Gabrielly, Geovanna, Yasmin"
"Turma: 2 ano B informática"

from programaSoSMulher import *
# 1. LOCALIZAÇÃO DA VÍTIMA
localizacao_vitima = localizacao("Rua 8.7600,63.9000","Rua das Flores","Centro","100","23/09/2026 14:30")

# 2. LOCALIZAÇÃO DO AGRESSOR
localizacao_agressor = localizacao("-8.7610,-63.9010","Rua Brasil","Centro","200","23/09/2026 14:35")

# 3. TORNOZELEIRA DO AGRESSOR
tornozeleira_agressor = tornozeleira("-8.7610,-63.9010","Rua Brasil","Centro","200","23/09/2026 14:35",["-8.7600,-63.9000"])

# 4. AGRESSOR
agressor1 = agressor("João","12345678900",tornozeleira_agressor,localizacao_agressor)

# 5. VÍTIMA
vitima1 = vitima("Maria","98765432100","1234","MPU001",agressor1,"76800000")

# adicionando a localização da vítima
vitima1.adicionar_localizacao(localizacao_vitima)

# 6. OPERADOR
operador1 = operador("Ana","11111111111","4321","Central de Atendimento")

# 7. MPU
mpu1 = mpu("MPU001",vitima1,agressor1,"200 metros","23/09/2026","ativa")

# 8. BOTÃO DE EMERGÊNCIA
botao1 = botao_emergencia(localizacao_vitima,"Alerta de emergência","14:40")

# 9. OCORRÊNCIA
ocorrencia1 = ocorrencia("23/09/2026 14:40","em andamento",vitima1,agressor1,localizacao_vitima)

# 10. VIATURA
viatura1 = viatura("Policial Carlos","ABC1D23",localizacao("-8.7620,-63.9020","Rua Central","Centro","300","23/09/2026 14:45"))
print(vitima1.nome)
print(vitima1.cpf)
print(vitima1.numeroMPU)

print("-------AGRESSOR------")
print(agressor1.getnome())
print(agressor1.getcpf())
print(agressor1.getlocalizacao())

print("-------LOCALIZAÇÃO DA VÍTIMA------")
print(localizacao_vitima.getcoordenadas())

print("-----MPU-----")
mpu1.consultarMPU()

print("------OCORRÊNCIA--------")
ocorrencia1.registros_ocorrencia()

print("-----BOTÃO DE EMERGÊNCIA-------")
botao1.enviar_localizacao()
botao1.emitir_alerta()

print("\n--------VIATURA------")
viatura1.receber_ocorrencia(ocorrencia1)

print("\n------TORNOZELEIRA-------")
tornozeleira_agressor.emitir_alerta()

print("\n-------OPERADOR-------")

operador1.cadastrar_usuario(vitima1)

operador1.dados_Agressor(agressor1)

operador1.receber_alerta("Agressor próximo da vítima")

operador1.localizar_vitima(localizacao_vitima)

operador1.localizar_agressor(localizacao_agressor)

print("\n------SOS-------")
vitima1.acionar_sos_sos(botao1)


print("\n-------ATUALIZANDO OCORRÊNCIA-------")

ocorrencia1.atualizar_status("em andamento")

ocorrencia1.encaminhar_ocorrencia(operador1)

viatura1.receber_ocorrencia(ocorrencia1)

viatura1.finalizar_ocorrencia(ocorrencia1)

print("\n------ATUALIZANDO VIATURA-------")

viatura1.atualizar_localizacao("-8.7630,-63.9030","Rua Nova","Centro","400","23/09/2026 15:00")