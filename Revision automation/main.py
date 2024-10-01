import os
import shutil

def contem_substring(string, substring):
    return substring in string

def comeca_com_numero(nome):
    return nome[0].isdigit()

def criar_pasta_antigos(diretorio):
    caminho_antigos = os.path.join(diretorio, "_Antigos")
    os.makedirs(caminho_antigos, exist_ok=True)

def mover_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho_atual = os.path.join(diretorio, item)

        if os.path.isdir(caminho_atual):
            if comeca_com_numero(item):
                criar_pasta_antigos(caminho_atual)
                mover_arquivos(caminho_atual)
        elif contem_substring(item, "R0"):
            for i in range(100):
                sufixo = f"R{i:02d}"
                sufixo_correspondente = f"R{i + 1:02d}"
                
                if sufixo in item:
                    novo_nome = item.replace(sufixo, sufixo_correspondente)
                    caminho_arquivo = os.path.join(diretorio, novo_nome)
                    
                    if os.path.exists(caminho_arquivo):
                        caminho_antigos = os.path.join(diretorio, "_Antigos", item)
                        shutil.move(caminho_atual, caminho_antigos)
                        print(f"Movido: {caminho_atual} -> {caminho_antigos}")
                        break

if __name__ == "__main__":
    diretorio = input("Digite o caminho do diretório: ")
    mover_arquivos(diretorio)
    print("Processo concluído.")
