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
        time.sleep(1)

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

# Aguardar horário
print("Esperando dar 17h...")
registrar_log("Aguardando 17h...")
esperar_ate_horario(12, 93)
print("É 17h! Executando ações...")
registrar_log("Executando ações às 17h.")

# Automação de busca (Ctrl+F)
pyautogui.press('f5')
registrar_log("Pressionado F5")
time.sleep(2)

pyautogui.hotkey('ctrl', 'f')
registrar_log("Pressionado Ctrl+F")
time.sleep(0.8)

pyautogui.write(termo_de_busca, interval=0.05)
registrar_log(f"Termo digitado: {termo_de_busca}")
time.sleep(0.5)

pyautogui.press('enter')
registrar_log("Pressionado Enter")
time.sleep(0.3)

# Apenas apaga o conteúdo da barra de busca (mantém aberta)
pyautogui.hotkey('ctrl', 'a')  # Seleciona tudo
time.sleep(0.1)
pyautogui.press('backspace')   # Apaga o texto
registrar_log("Texto da barra de busca apagado")

# Procurar imagem na tela
print("Procurando o item na tela por imagem...")
registrar_log("Procurando imagem do item na tela...")

# Caminho da imagem do item
imagem_alvo = f"{termo_de_busca.lower()}.png"

try:
    localizacao = pyautogui.locateCenterOnScreen(imagem_alvo, confidence=0.8)
    if localizacao:
        print(f"Item encontrado na posição: {localizacao}. Iniciando cliques...")
        registrar_log(f"Item encontrado na posição: {localizacao}")

        for i in range(8):
            pyautogui.click(localizacao)
            registrar_log(f"Clique {i+1} na posição: {localizacao}")
            print(f"Clique {i+1} feito na posição: {localizacao}")
            time.sleep(5)
    else:
        print("Item não encontrado na tela.")
        registrar_log("Item não encontrado na tela.")
except Exception as e:
    print("Erro ao localizar imagem:", e)
    registrar_log(f"Erro ao localizar imagem: {e}")

print("Ações finalizadas.")
registrar_log("Todos os cliques realizados.")
