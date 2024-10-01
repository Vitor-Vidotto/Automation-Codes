import json
import subprocess
import time
import os

# Função para ler o arquivo JSON e obter a lista de diretórios
def get_directories_from_json(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo JSON não encontrado: {file_path}")

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            directories = data.get('directories', [])
            if not isinstance(directories, list):
                raise ValueError("O campo 'directories' deve ser uma lista.")
            return directories
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao decodificar o JSON: {e}")

# Função para executar o programa com um diretório
def run_program_with_directory(directory):
    command = ['./main.exe']
    
    try:
        # Execute o programa
        print(f"Iniciando o programa para o diretório: {directory}")
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Enviar o diretório para o programa
        process.stdin.write(directory + '\n')
        process.stdin.flush()
        
        # Aguarda o término do programa
        stdout, stderr = process.communicate()
        
        # Verificar se o programa terminou com sucesso
        if process.returncode != 0:
            print(f"Erro ao executar o programa para o diretório {directory}: {stderr}")
        else:
            print(f"Saída do programa para o diretório {directory}: {stdout}")

        # Espera até que o processo seja realmente fechado
        while process.poll() is None:
            time.sleep(0.1)

    except Exception as e:
        print(f"Ocorreu um erro ao executar o programa: {e}")

def main():
    # Caminho para o arquivo JSON
    json_file_path = 'directories.json'
    
    try:
        # Obtendo a lista de diretórios do arquivo JSON
        directories = get_directories_from_json(json_file_path)
        
        if not directories:
            print("Nenhum diretório para processar.")
            return
        
        # Log dos diretórios lidos do JSON
        print("Diretórios lidos do arquivo JSON:")
        for directory in directories:
            print(f"- {directory}")
        
        # Rodando o programa de limpeza para cada diretório
        for directory in directories:
            print(f"Iniciando processamento para o diretório: {directory}")
            run_program_with_directory(directory)
            
            # Aguarda 1 segundo entre as execuções
            time.sleep(1)
        
        print("Todos os diretórios foram processados.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
