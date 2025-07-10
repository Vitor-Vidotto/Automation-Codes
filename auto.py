import pyautogui
import datetime
import time
import os
import random

# Caminho da área de trabalho
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
log_path = os.path.join(desktop, "log_cliques.txt")

# Função para registrar log
def registrar_log(texto):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {texto}\n")

# Esperar até 17h00
def esperar_ate_17h():
    while True:
        agora = datetime.datetime.now()
        if agora.hour == 14 and agora.minute == 3:
            break
        time.sleep(1)

print("Esperando dar 17h...")
registrar_log("Aguardando 17h...")
esperar_ate_17h()
print("É 17h! Executando ações...")
registrar_log("Executando ações às 17h.")

# Pressionar F5
pyautogui.press('f5')
registrar_log("Pressionado F5")
time.sleep(4)

# Pressionar Ctrl + F
pyautogui.hotkey('ctrl', 'f')
registrar_log("Pressionado Ctrl+F")
time.sleep(0.8)

# Digitar o termo
termo_de_busca = 'Fuji'
pyautogui.write(termo_de_busca, interval=0.05)
registrar_log(f"Termo digitado: {termo_de_busca}")
time.sleep(0.5)

# Pressionar Enter
pyautogui.press('enter')
registrar_log("Pressionado Enter")
time.sleep(1)

# Esperar posicionamento
print("Posicione o mouse no botão desejado. Esperando 5 segundos...")
registrar_log("Esperando posicionamento do mouse para cliques...")
time.sleep(5)

# Fazer 5 cliques com pausas variadas
for i in range(5):
    pos = pyautogui.position()
    pyautogui.click()
    registrar_log(f"Clique {i+1} na posição: {pos}")
    print(f"Clique {i+1} feito na posição: {pos}")
    pausa = 5
    print(f"Proximo clique em 5 segundos") 
    time.sleep(pausa)

print("Todos os cliques realizados.")
registrar_log("Todos os cliques realizados.")
