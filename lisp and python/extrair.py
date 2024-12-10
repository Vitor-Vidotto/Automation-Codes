import pyautogui
import time
import os
import json

# Função para carregar os diretórios a partir de um arquivo JSON
def carregar_directorios():
    # Caminho do arquivo JSON onde os diretórios são armazenados
    caminho_json = 'directories.json'
    
    # Verificar se o arquivo existe
    if not os.path.exists(caminho_json):
        print(f"O arquivo {caminho_json} não foi encontrado.")
        exit()
    
    # Carregar os dados do arquivo JSON
    with open(caminho_json, 'r') as f:
        dados = json.load(f)
        
    return dados['diretorio_pasta'], dados['diretorio_salvar']

# Carregar os diretórios
diretorio_pasta, diretorio_salvar = carregar_directorios()

# Função para processar cada arquivo DWG
def processar_arquivo(nome_arquivo_dwg):
    # Passo 1: Abrir o Explorador de Arquivos
    time.sleep(3)
    pyautogui.hotkey('win', 'e')  # Abre o explorador de arquivos
    time.sleep(1)  # Aguarda o tempo necessário para o explorador abrir

    # Passo 2: Escrever o caminho da pasta no Explorador de Arquivos
    pyautogui.write(diretorio_pasta)
    pyautogui.press('enter')  # Pressiona Enter para ir para a pasta
    time.sleep(1)  # Aguarda um pouco o explorador carregar a pasta

    # Passo 3: Navegar com a tecla Tab (6 vezes) para a área de arquivos
    for _ in range(6):
        pyautogui.press('tab')

    time.sleep(1)  # Aguarda um pouco para garantir que o foco esteja na lista de arquivos

    # Passo 4: Escrever o caminho completo do arquivo DWG
    caminho_arquivo_dwg = os.path.join(diretorio_pasta, nome_arquivo_dwg)  # Caminho completo
    pyautogui.write(caminho_arquivo_dwg)  # Escreve o caminho completo do arquivo DWG
    pyautogui.press('enter')  # Pressiona Enter para abrir o arquivo DWG
    time.sleep(2)  # Aguarda o arquivo abrir

    # Passo 5: Realizar as ações necessárias no arquivo DWG
    pyautogui.click(x=1255, y=780)  # Clica em um ponto específico
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(x=1198, y=472)  # Mover para a posição onde o comando é inserido
    pyautogui.write("extr")  # Escrever o comando (ajuste conforme necessário)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

    # Passo 6: Salvar o arquivo com o nome do arquivo DWG
    nome_arquivo_salvar = os.path.join(diretorio_salvar, f"{nome_arquivo_dwg}.txt")
    pyautogui.write(nome_arquivo_salvar)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # Passo 7: Fechar o arquivo e a janela
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')

    print(f"Arquivo {nome_arquivo_dwg} processado e salvo como {nome_arquivo_dwg}.txt")

# Passo 8: Processar todos os arquivos DWG na pasta
def processar_todos_arquivos():
    # Listar todos os arquivos na pasta
    arquivos = os.listdir(diretorio_pasta)

    # Filtrar apenas os arquivos DWG
    arquivos_dwg = [arquivo for arquivo in arquivos if arquivo.lower().endswith('.dwg')]

    # Processar cada arquivo DWG encontrado
    for arquivo_dwg in arquivos_dwg:
        print(f"Iniciando o processo para o arquivo: {arquivo_dwg}")
        processar_arquivo(arquivo_dwg)
        time.sleep(3)  # Aguarda um pouco antes de iniciar o próximo arquivo

# Executar a função para processar todos os arquivos
processar_todos_arquivos()
