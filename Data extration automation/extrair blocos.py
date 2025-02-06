import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def filtrar_csv():
    # Criando uma janela oculta (não precisa ser exibida)
    Tk().withdraw()

    # Pedindo para o usuário selecionar o arquivo de entrada (Excel)
    input_file = askopenfilename(title="Selecione o arquivo Excel", filetypes=[("Excel files", "*.xls;*.xlsx")])
    if not input_file:
        print("Nenhum arquivo de entrada selecionado.")
        return

    # Pedindo para o usuário selecionar o local e nome do arquivo de saída (com a extensão .csv)
    output_file = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Selecione onde salvar o arquivo filtrado")
    if not output_file:
        print("Nenhum arquivo de saída selecionado.")
        return

    try:
        # Tentando abrir o arquivo Excel com o motor correto
        if input_file.endswith('.xlsx'):
            df = pd.read_excel(input_file, engine='openpyxl')
        else:
            df = pd.read_excel(input_file, engine='xlrd')

        # Definindo as colunas a serem mantidas no arquivo filtrado
        colunas_desejadas = ['Name', 'Position X', 'Position Y', 'Position Z', 'Rotation', 'Scale X']

        # Filtrando as linhas com os nomes desejados na coluna 'Name' e que não tenham valores nulos ou vazios
        df_filtrado = df[df['Name'].notna() & df['Name'].str.contains('Line|AL_Bloco|14X19X44', na=False)]

        # Adicionando a condição de que pelo menos 2 colunas entre 'Position X', 'Position Y', 'Position Z', 'Rotation', 'Largura_Porta', 'Altura_Porta', 'Largura_Janela', 'Altura_Janela', 'Peitoril_Janela' devem estar preenchidas
        df_filtrado['num_validos'] = df_filtrado[['Name', 'Position X', 'Position Y', 'Position Z', 'Rotation', 'Scale X']].notna().sum(axis=1)

        df_filtrado = df_filtrado[df_filtrado['num_validos'] >= 2]

        # Garantindo que a filtragem considere apenas as colunas desejadas
        df_filtrado = df_filtrado[colunas_desejadas]

        # Salvando o arquivo filtrado em formato CSV
        df_filtrado.to_csv(output_file, index=False, encoding='utf-8')

        print(f"Arquivo filtrado e salvo em {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

# Chamada da função
filtrar_csv()
