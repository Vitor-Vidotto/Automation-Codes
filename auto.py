import pyautogui
import datetime
import time
import os
import sys
import threading
import ntplib
from datetime import timezone, timedelta

# Função para obter horário de Brasília via NTP
def get_ntp_brasilia():
    try:
        cliente = ntplib.NTPClient()
        resposta = cliente.request('a.st1.ntp.br')  # Servidor brasileiro
        utc = datetime.datetime.fromtimestamp(resposta.tx_time, timezone.utc)
        brasilia = utc - timedelta(hours=3)
        return brasilia
    except:
        print("❌ Erro ao sincronizar com o NTP. Usando horário local.")
        return datetime.datetime.now()  # fallback

ajuste_final = None  # será definido pelo usuário

# Exibição do relógio sincronizado enquanto usuário informa o ajuste
def exibir_relogio():
    while ajuste_final is None:
        agora = get_ntp_brasilia()
        print(f"\r⏰ Horário NTP de Brasília: {agora.strftime('%H:%M:%S')}", end="", flush=True)
        time.sleep(1)

# Inicia o relógio em uma thread paralela
thread_relogio = threading.Thread(target=exibir_relogio)
thread_relogio.start()

# Pergunta ao usuário
while True:
    try:
        print("\nDigite quantos segundos o sistema está adiantado (+) ou atrasado (-) em relação ao real:")
        segundos = int(input("↕ Atraso ou adiantamento (em segundos): "))
        ajuste_final = segundos
        break
    except ValueError:
        print("❌ Entrada inválida. Digite um número inteiro.")

# Aplica ajuste
atraso = timedelta(seconds=ajuste_final)

def clicar_na_imagem(nome_arquivo, confidence=0.8):
    try:
        local = pyautogui.locateCenterOnScreen(nome_arquivo, confidence=confidence)
        if not local:
            print(f"❌ Imagem {nome_arquivo} não encontrada na tela.")
            return
        print(f"Clicando em {nome_arquivo} em {local}")
        pyautogui.click(local)
    except pyautogui.ImageNotFoundException:
        print(f"❌ Imagem {nome_arquivo} não encontrada (exceção capturada).")


# Caminho absoluto mesmo no PyInstaller
def caminho_absoluto(rel_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

# Função que espera até horário alvo usando NTP + ajuste
def esperar_ate_horario(hora, minuto):
    while True:
        agora_brasilia = get_ntp_brasilia() + atraso
        print(f"\r⏳ Aguardando: {agora_brasilia.strftime('%H:%M:%S')}", end="", flush=True)

        if agora_brasilia.hour == hora and agora_brasilia.minute == minuto:
            print()  # nova linha
            break
        time.sleep(1)

# Seletor de restaurante
opcoes = ['Fuji', 'Zendai', 'Koiumi', 'Campolim', 'Real - Campolim']
print("Selecione o restaurante para pesquisa:")
for i, nome in enumerate(opcoes, 1):
    print(f"{i}. {nome}")

while True:
    try:
        escolha = int(input("Digite o número correspondente: "))
        if 1 <= escolha <= len(opcoes):
            termo_de_busca = opcoes[escolha - 1]
            break
        else:
            print("Escolha inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

print(f"Restaurante escolhido: {termo_de_busca}")

# Espera até 17h (ajustável)
print("Esperando dar 17h (horário de Brasília)...")

print("É 17h! Executando ações...")
time.sleep(3)

# Executa automação
pyautogui.press('f5')
time.sleep(1.5)
pyautogui.hotkey('ctrl', 'f')
time.sleep(0.1)
pyautogui.write(termo_de_busca, interval=0.05)
pyautogui.press('enter')
time.sleep(0.1)
pyautogui.press("esc")
time.sleep(0.1)
pyautogui.press('enter')
time.sleep(0.8)


cliques_por_opcao = {
    "1": ["tab", "space", "tab", "tab", "space", "tab", "tab", "space"],
    "2": ["tab", "tab", "space", "tab"],
    
    "3": ["tab", "space", "tab", "space"],
    "4": ["tab", "space", "tab", "space", "tab", "space"],
    "5": ["tab", "space", "tab", "space", "tab", "tab", "space"]
}
 
opcao = str(opcoes.index(termo_de_busca) + 1)
cliques = cliques_por_opcao.get(opcao, [])

print(f"Iniciando sequência de teclas da opção {opcao}...")
for i, tecla in enumerate(cliques, 1):
    pyautogui.press(tecla)
    print(f"✔ Tecla {i} pressionada: {tecla.upper()}")
    time.sleep(0.1)

pyautogui.press("down")
pyautogui.press("down")
pyautogui.press("down")
pyautogui.press("down")

clicar_na_imagem(caminho_absoluto("imagens/verificar.png"))
time.sleep(0.5)
pyautogui.press("enter")
