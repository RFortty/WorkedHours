from datetime import date, datetime

# total dias por ano
ano = 365
# total semanas por ano
semanas = 52
# total horas trabalhadas por dia
total_horas_dia = 8
# total dias de trabalho
total_dias_trab = 5

nome = input("\n.....................Informe seu Nome: ")
adm = (input("\n.........Informe sua data de admissão: ")) # 26/07/2013
sal_base = float(input(".............Informe seu Salário Base: R$ ")) # R$3.025,16
aux_doença = (sal_base + (sal_base * 0.07)) * (91/100)
sal_base = aux_doença
cesta_basica = float(input("......Informe o valor da Cesta Básica: R$ "))

data_hoje = datetime.today()
data_hoje_formatada = data_hoje.strftime('%d/%m/%Y') # Converte Data em String

data_adm = datetime.strptime(adm, '%d/%m/%Y') # Converte String em Data
data_dif = data_hoje - data_adm

quinquenio = (data_dif.days // ano) // 5
print(f">> Qtde. Quinquenio:= {quinquenio}")

# quinquenio = int(input("Informe quantos Quinquenios vc possue: ")) # +5% a cada 5 anos trabalhados
# Cálculo do Quinquenio
if quinquenio == 0:
    total_quin = 0
elif quinquenio == 1:
    total_quin = sal_base * (5/100)
elif quinquenio == 2:
    total_quin = sal_base * (10/100)
elif quinquenio == 3:
    total_quin = sal_base * (15/100)
elif quinquenio == 4:
    total_quin = sal_base * (20/100)
elif quinquenio == 4:
    total_quin = sal_base * (25/100)
elif quinquenio == 6:
    total_quin = sal_base * (30/100)
else:
    total_quin = 0

#Calculando Total de Horas trabalhadas Semanal
total_horas_sem = total_horas_dia * total_dias_trab
#Calculando Total de Horas trabalhadas Mensal
total_horas_mes = 220
#Calculando Total de Horas trabalhadas Anual
total_horas_ano = semanas * total_horas_sem

#Calculando o Salário por hora
sal_hora = (sal_base + total_quin) / 200
#Calculando o Salário por hora 50%
sal_hora50 = ((sal_base + total_quin) / 200) * 1.5
#Calculando o Salário por hora 70%
sal_hora70 = ((sal_base + total_quin) / 200) * 1.7
#Calculando o Salário por hora 100%
sal_hora100 = ((sal_base + total_quin) / 200) * 2
#Calculando o Salário por hora Adicional Noturno
sal_hora_AdNoturno = ((sal_base + total_quin) / 200) * 0.2
#Calculando Periculosidade = Salário * 30%
periculosidade = sal_base * (30 / 100)
#Calculando Insalubridade = Salário * 20%
insalubridade = 0

#Calculando o Salário diário
sal_dia = sal_hora * total_horas_dia
#Calculando o Salário semanal
sal_sem = sal_dia * total_dias_trab
#Calculando o Salário mensal
sal_mes = sal_sem * total_horas_sem

total_bruto = sal_base + cesta_basica + total_quin + periculosidade

print(f'\n[ Informações do Funcionário: {nome} ]\n')
print('>> Total de Horas Trabalhadas por Dia: ',total_horas_dia, 'h')
print('>> Total de Horas Trabalhadas Semanal: ',total_horas_sem, 'h')
print('>> Total de Horas Trabalhadas Mensal : ',total_horas_mes, 'h')
print('\n')
print('---------------[ R E C E I T A S ]---------------')
print(f'\n[ Informações do Salário: {nome} ]\n')
print(f'>> Salário Base .....................: R$ {sal_base:_.2f}')
print(f'>> Cesta Básica .....................: R$ {cesta_basica:_.2f}')
print(f'>> Quinquenio .......................: R$ {total_quin:_.2f}')
print(f'>> Periculosidade ...................: R$ {periculosidade:_.2f}')
print('\n')
print('>> ..................Salário por Hora: R$ {:,.2f}'.format(sal_hora))
print('>> .............Salário por Hora 50% : R$ {:,.2f}'.format(sal_hora50))
print('>> .............Salário por Hora 70% : R$ {:,.2f}'.format(sal_hora70))
print('>> .............Salário por Hora 100%: R$ {:,.2f}'.format(sal_hora100))
print(f'>> Salário por Hora Adicional Noturno: R$ {sal_hora_AdNoturno:_.2f}')
print('\n')
print(f'>> T O T A L Bruto à Receber__: R$ {total_bruto:_.2f}'.replace('.',',').replace('_','.'))
print('\n')
print('--------------[ D E S C O N T O S ]--------------')
print('\n')

Iprem = float(input(".........Informe o valor do IPREM: R$ ")) # R$465,88
IR_Fonte = float(input("......Informe o valor do IR/Fonte: R$ ")) # R$87,45
IR_dependente = float(input("Informe o valor do IR Dependentes: R$ ")) # R$189,59

total_desc = Iprem + IR_Fonte + IR_dependente
total_liq = total_bruto - total_desc

print('\n')
print(f'>> T O T A L de Descontos_____: R$ {total_desc:_.2f}'.replace('.',',').replace('_','.'))
print('\n')
print('..................................................')
print(f'>> T O T A L Líquido à Receber: R$ {total_liq:_.2f}'.replace('.',',').replace('_','.'))
print('..................................................')
print('\n')
