import pyautogui
import datetime
import time
import os
import sys

# Função para obter caminho absoluto mesmo em .exe do PyInstaller
def caminho_absoluto(rel_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

# Caminho da área de trabalho
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
log_path = os.path.join(desktop, "log_cliques.txt")


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

print(f"Restaurante escolhido: {termo_de_busca}")

start_time = time.time()

# Espera até o horário definido
print("Esperando dar 17h...")
esperar_ate_horario(17, 00)  # Altere para o horário desejado

print("É 17h! Executando ações...")


# ⏱️ Início da contagem do tempo
time.sleep(5)
# Automação de busca (Ctrl+F)
pyautogui.press('f5')
time.sleep(1)

pyautogui.hotkey('ctrl', 'f')
time.sleep(0.2)

pyautogui.write(termo_de_busca, interval=0.05)
time.sleep(0.2)

pyautogui.press('enter')
time.sleep(0.2)
pyautogui.press("esc")
time.sleep(0.2)
pyautogui.press('enter')

# Mapeamento de cliques por opção
time.sleep(0.2)
cliques_por_opcao = {
    "1": ["tab", "space", "tab", "tab", "space", "tab", "tab", "space", "tab", "tab", "space", "enter"],
    "2": ["tab", "tab", "space", "tab", "tab", "tab", "space", "enter"],
    "3": ["tab", "space", "tab", "space", "tab", "space", "enter"]
}

# Determinar opção com base no termo de busca
opcao = str(opcoes.index(termo_de_busca) + 1)
cliques = cliques_por_opcao.get(opcao, [])

print(f"Iniciando sequência de teclas da opção {opcao}...")

for i, tecla in enumerate(cliques, 1):
    pyautogui.press(tecla)
    print(f"✔ Tecla {i} pressionada: {tecla.upper()}")
    time.sleep(0.1)

# ⏱️ Fim da contagem e exibição
tempo_total = time.time() - start_time
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)

mensagem_tempo = f"Tempo de execução: {minutos} min {segundos} seg."
print(mensagem_tempo)
