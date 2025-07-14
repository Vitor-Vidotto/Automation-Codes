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

# Espera até o horário definido
print("Esperando dar 17h...")
registrar_log("Aguardando 17h...")
esperar_ate_horario(17, 00)  # Altere para o horário desejado
print("É 17h! Executando ações...")
registrar_log("Executando ações às 17h.")

# ⏱️ Início da contagem do tempo
start_time = time.time()

# Automação de busca (Ctrl+F)
pyautogui.press('f5')
registrar_log("Pressionado F5")
time.sleep(1)

pyautogui.hotkey('ctrl', 'f')
registrar_log("Pressionado Ctrl+F")
time.sleep(0.1)

pyautogui.write(termo_de_busca, interval=0.05)
registrar_log(f"Termo digitado: {termo_de_busca}")
time.sleep(0.1)

pyautogui.press('enter')
registrar_log("Pressionado Enter")
time.sleep(0.1)

# Limpa o campo de busca
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.1)
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
cliques_por_opcao = {
    "1": [(978, 498), (988, 588), (992, 673), (990, 763), (989, 843), (983, 934), (992, 1011)],
    "2": [(967, 464), (957, 545), (960, 625), (953, 713), (946, 790)],
    "3": [(989, 486), (986, 569)]
}

# Determinar opção com base no termo de busca
opcao = str(opcoes.index(termo_de_busca) + 1)
cliques = cliques_por_opcao.get(opcao, [])

print(f"Iniciando sequência de cliques da opção {opcao}...")
registrar_log(f"Iniciando sequência de cliques da opção {opcao}...")

for i, (x, y) in enumerate(cliques, 1):
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()
    registrar_log(f"Clique {i} em coordenada: ({x}, {y})")
    print(f"✔ Clique {i} realizado em ({x}, {y})")

pyautogui.press(['down', 'down', 'down'])
time.sleep(0.1)  # Espera a tela carregar

for nome in ["verificar", "concluido"]:
    try:
        print(f"Procurando '{nome}.png'...")
        pyautogui.screenshot(f"debug_{nome}.png")  # Captura da tela para depuração
        pos = pyautogui.locateCenterOnScreen(f"{nome}.png", confidence=0.8)
        if pos:
            pyautogui.click(pos)
            registrar_log(f"Clique na imagem: {nome}.png")
            print(f"✔ Clique realizado em '{nome}.png'")
        else:
            print(f"❌ Imagem '{nome}.png' não encontrada.")
            registrar_log(f"Imagem '{nome}.png' não encontrada.")
    except Exception as e:
        print(f"Erro ao buscar imagem {nome}.png: {e}")
        registrar_log(f"Erro ao buscar imagem {nome}.png: {e}")

# ⏱️ Fim da contagem e exibição
tempo_total = time.time() - start_time
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)
mensagem_tempo = f"Tempo de execução: {minutos} min {segundos} seg."
print(mensagem_tempo)
registrar_log(mensagem_tempo)
