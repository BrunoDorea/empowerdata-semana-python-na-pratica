import yfinance as yf
import pyautogui
import pyperclip
import time

ticker = input("Digite o código da ação: ")
ticker = ticker.upper()
dados = yf.Ticker(ticker).history("1y")

fechamento = dados.Close

fechamento.plot()

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(f"Ação: {ticker}")
print(f"A cotação máxima é: R$ {maxima:.2f}")
print(f"A cotação mínima é: R$ {minima:.2f}")
print(f"A cotação atual é: R$ {atual:.2f}")

# pause de 2 segundos
pyautogui.PAUSE = 3

# Abrir o navegador
time.sleep(3)

# Abrir nova aba no navegador (CTRL + T)
pyautogui.hotkey("ctrl", "t")

# Digitar o endereço do gmail, 'Enter'
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

# Clicar no botão 'Escrever'
pyautogui.click(x=75, y=215)

# Digitar o destinatario, 'Tab'
pyperclip.copy('semanapython@gmail.com')
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar o assunto, 'Tab'
pyperclip.copy('Análises diárias')
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar a mensagem do email
mensagem = f"""
Prezado Gestor,

Segue as análises, conforme solicitado da ação {ticker} referente ao último ano.

Cotação máxima: R$ {maxima:.2f}
Cotação mínima: R$ {minima:.2f}
Cotação atual: R$ {atual:.2f}

Qualquer dúvida, estou à disposição!

Atte.

"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar em 'Enviar'
# pyautogui.click(x=590, y=1000)
