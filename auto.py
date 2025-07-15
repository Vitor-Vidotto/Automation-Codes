import pyautogui

import datetime

import time

import os

# Caminho da área de trabalho

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

log_path = os.path.join(desktop, "log_cliques.txt")

# Função para registrar log

def registrar_log(texto):

    with open(log_path, "a", encoding="utf-8") as f:

        f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {texto}\n")

# Função para esperar até horário definido

def esperar_ate_horario(hora, minuto):

    while True:

        agora = datetime.datetime.now()

        if agora.hour == hora and agora.minute == minuto:

            break

# Seletor de restaurante

opcoes = ['Fuji', 'Zendai', 'Columbia']

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

registrar_log(f"Restaurante selecionado: {termo_de_busca}")

print(f"Restaurante escolhido: {termo_de_busca}")

start_time = time.time()
# Espera até o horário definido

print("Esperando dar 17h...")

registrar_log("Aguardando 17h...")

esperar_ate_horario(17, 00)  # Altere para o horário desejado

print("É 17h! Executando ações...")

registrar_log("Executando ações às 17h.")

# ⏱️ Início da contagem do tempo


# Automação de busca (Ctrl+F)

pyautogui.press('f5')

registrar_log("Pressionado F5")

time.sleep(1)

pyautogui.hotkey('ctrl', 'f')

registrar_log("Pressionado Ctrl+F")

time.sleep(0.2)

pyautogui.write(termo_de_busca, interval=0.05)

registrar_log(f"Termo digitado: {termo_de_busca}")

time.sleep(0.2)

pyautogui.press('enter')

registrar_log("Pressionado Enter")

time.sleep(0.2)

# Limpa o campo de busca

pyautogui.hotkey('ctrl', 'a')

time.sleep(0.2)

pyautogui.press('backspace')

registrar_log("Texto da barra de busca apagado")

pyautogui.press('esc')

# 🖼️ Tentar clicar na imagem do restaurante (ex: zendai.png)

imagem_opcao = termo_de_busca.lower() + ".png"

try:

    print(f"Procurando imagem do restaurante: '{imagem_opcao}'...")

    pos = pyautogui.locateCenterOnScreen(imagem_opcao, confidence=0.8)

    if pos:

        pyautogui.click(pos)

        registrar_log(f"Clique na imagem do restaurante: {imagem_opcao}")

        print(f"✔ Clique realizado na imagem '{imagem_opcao}'")

        time.sleep(0.3)

    else:

        print(f"❌ Imagem '{imagem_opcao}' não encontrada.")

        registrar_log(f"Imagem '{imagem_opcao}' não encontrada.")

except Exception as e:

    print(f"Erro ao buscar imagem {imagem_opcao}: {e}")

    registrar_log(f"Erro ao buscar imagem {imagem_opcao}: {e}")


# Mapeamento de cliques por opção
time.sleep(4)
cliques_por_opcao = {
    "1": ["tab", "space", "tab", "tab", "space", "tab", "tab", "space", "tab", "tab", "space", "enter"],
    "2": ["tab", "tab", "space", "tab","tab","tab", "space", "enter"],
    "3": ["tab", "space", "tab", "space", "tab", "space", "enter"]
}


# Determinar opção com base no termo de busca

opcao = str(opcoes.index(termo_de_busca) + 1)

cliques = cliques_por_opcao.get(opcao, [])

print(f"Iniciando sequência de teclas da opção {opcao}...")
registrar_log(f"Iniciando sequência de teclas da opção {opcao}...")

sequencia = cliques_por_opcao.get(opcao, [])

for i, tecla in enumerate(sequencia, 1):
    pyautogui.press(tecla)
    registrar_log(f"Tecla {i} pressionada: {tecla.upper()}")
    print(f"✔ Tecla {i} pressionada: {tecla.upper()}")
    time.sleep(0.1)

# ⏱️ Fim da contagem e exibição

tempo_total = time.time() - start_time

minutos = int(tempo_total // 60)

segundos = int(tempo_total % 60)

mensagem_tempo = f"Tempo de execução: {minutos} min {segundos} seg."

print(mensagem_tempo)

registrar_log(mensagem_tempo)
