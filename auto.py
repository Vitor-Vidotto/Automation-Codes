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


# Procurar imagem na tela
print("Procurando o item na tela por imagem...")
registrar_log("Procurando imagem do item na tela...")

# Executar sequência de cliques por imagem
print("Iniciando sequência de cliques por imagem...")
registrar_log("Iniciando sequência de cliques por imagem...")

prefixo_imagem = termo_de_busca.lower()
max_cliques = 10  # Defina o máximo de tentativas de clique sequencial

for indice_clique in range(1, max_cliques + 1):
    imagem_clique = f"{prefixo_imagem}_click{indice_clique}.png"
    try:
        posicao = pyautogui.locateCenterOnScreen(imagem_clique, confidence=0.8)
        if posicao:
            pyautogui.click(posicao)
            registrar_log(f"Clique na imagem: {imagem_clique} em {posicao}")
            print(f"Clique {indice_clique} realizado na posição: {posicao}")
            time.sleep(1.5)
        else:
            print(f"Imagem {imagem_clique} não encontrada. Pulando para o próximo.")
            registrar_log(f"Imagem {imagem_clique} não encontrada. Pulando.")
            continue
    except Exception as e:
        print(f"Erro ao buscar imagem {imagem_clique}: {e}")
        registrar_log(f"Erro ao buscar imagem {imagem_clique}: {e}")

# Clique em verificar
try:
    print("Procurando 'verificar.png'...")
    verificar = pyautogui.locateCenterOnScreen("verificar.png", confidence=0.8)
    if verificar:
        pyautogui.click(verificar)
        registrar_log("Clique na imagem: verificar.png")
        print("Clique realizado em 'verificar.png'")
        time.sleep(2)
    else:
        print("Imagem 'verificar.png' não encontrada.")
        registrar_log("Imagem 'verificar.png' não encontrada.")
except Exception as e:
    print(f"Erro ao buscar imagem verificar.png: {e}")
    registrar_log(f"Erro ao buscar imagem verificar.png: {e}")

# Clique em concluído
try:
    print("Procurando 'concluido.png'...")
    concluido = pyautogui.locateCenterOnScreen("concluido.png", confidence=0.8)
    if concluido:
        pyautogui.click(concluido)
        registrar_log("Clique na imagem: concluido.png")
        print("Clique realizado em 'concluido.png'")
    else:
        print("Imagem 'concluido.png' não encontrada.")
        registrar_log("Imagem 'concluido.png' não encontrada.")
except Exception as e:
    print(f"Erro ao buscar imagem concluido.png: {e}")
    registrar_log(f"Erro ao buscar imagem concluido.png: {e}")

print("Ações finalizadas.")
registrar_log("Todos os cliques realizados.")
