import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            name, ext = os.path.splitext(filename)
            parts = name.rsplit('-', 1)  # Divide a partir do último hífen
            
            if len(parts) > 1:
                new_name = parts[0].strip()  # Mantém a parte antes do último hífen
            else:
                new_name = name
            
            new_filename = new_name + ext
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print(f'Renomeado: {filename} -> {new_filename}')

if __name__ == '__main__':
    directory = input('insira o Diretorio: ').strip()
    if os.path.isdir(directory):
        rename_files_in_directory(directory)
    else:
        print('O diretorio providenciado não foi encontrado.')
