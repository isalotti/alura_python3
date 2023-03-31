from datetime import datetime

import pytz
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')

print(data_e_hora_sao_paulo_em_texto)

#Para mostrar todos os time zone disponiveis:
# for tz in pytz.all_timezones:
#     print(tz)