from datetime import datetime, timezone , timedelta

diferenca = timedelta(hours=-3)  # -3 -> UTC-3 = Sao Paulo

fuso_horario = timezone(diferenca)

data = datetime.today()
data_txt = data.strftime('%d/%m/%Y')

print(data_txt)

data_hora = datetime.now()
data_hora_txt = data_hora.strftime('%d/%m/%Y %H:%M:%S')

print(data_hora_txt)

## texto -> Data

data_e_hora_em_texto = '31/03/2023 14:40:09'
data_e_hora_conv = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M:%S')

## fuso

print(fuso_horario)

data_e_hora_sao_paulo = data_hora.astimezone(fuso_horario)
data_e_hora_sao_paulo_txt = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')

print(data_e_hora_sao_paulo_txt)