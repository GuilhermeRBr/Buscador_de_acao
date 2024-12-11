import yfinance as yf
import pyautogui as gui
import pyperclip as pc
import webbrowser as web
from time import sleep


ticket = str(input('Digite o ticket da ação (ex.: UBER): ').upper())
dados = yf.Ticker(ticket).history(start='2023-03-10', end='2023-04-10')
fechamento = dados.Close

#resultado:
maximo = round(fechamento.max(), 2) 
minimo = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

#Mensagens:
email = 'teste@exemplo.com'
assunto = f'Análise das ações: {ticket} no periodo 2020-05-10 a 2020-06-10 ' 
mensagem = f'''
Prezado gestor,

Seguem as análises solicitadas da ação {ticket}:

Cotação máxima: R${maximo}
Cotação mínima: R${minimo}
Valor médio: R${media}
Qualquer dúvida, estou à disposição!

Atenciosamente,
Gestor.

'''
#Automação:
gui.PAUSE = 3

web.open('www.gmail.com')
sleep(5)

#escrever:
gui.click(x=107, y=194)

#Colar email:
pc.copy(email)
gui.hotkey('ctrl', 'v')

#Colar assunto:
gui.hotkey('tab')
pc.copy(assunto)
gui.hotkey('ctrl', 'v')

#Colar mensagem:
gui.hotkey('tab')
pc.copy(mensagem)
gui.hotkey('ctrl', 'v')

#Enviar:
gui.hotkey('ctrl', 'enter')

#Fechar aba:
gui.hotkey('ctrl', 'w')
