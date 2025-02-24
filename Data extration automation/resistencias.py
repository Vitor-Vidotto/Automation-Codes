import pandas as pd
import tkinter as tk
from tkinter import filedialog
import math

def round_up_to_multiple(value, multiple=5):
    return math.ceil(value / multiple) * multiple

def get_fa_value(fbk):
    if 3 <= fbk <= 6:
        return "AAE5"
    elif 8 <= fbk <= 10:
        return "AAE8"
    elif 12 <= fbk <= 14:
        return "AAE12"
    elif 16 <= fbk <= 18:
        return "AAE16"
    elif 20 <= fbk <= 22:
        return "AAE20"
    elif 24 <= fbk <= 26:
        return "AAEE"
    return ""

def process_file():
    root = tk.Tk()
    root.withdraw()
    
    txt_path = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Text Files", "*.txt")])
    if not txt_path:
        print("Nenhum arquivo selecionado.")
        return
    
    save_path = filedialog.asksaveasfilename(title="Salvar como", defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if not save_path:
        print("Nenhum local de salvamento selecionado.")
        return
    
    with open(txt_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    headers = ["Niv", "Fbk", "Fgk", "Fa", "Fpk", "Fpk"]  # Definir colunas específicas
    data = []
    
    for line in lines[4:-1]:  # Pular as linhas iniciais e a última linha separadora
        values = line.split()
        if len(values) >= 9:  # Garantir que há colunas suficientes
            fbk = float(values[1])
            fa = get_fa_value(fbk)
            row = ["", fbk, round_up_to_multiple(float(values[8])), fa, float(values[5]), float(values[6])]
            data.append(row)
    
    df = pd.DataFrame(data, columns=headers)
    df.to_excel(save_path, index=False)
    print(f"Arquivo salvo em: {save_path}")

if __name__ == "__main__":
    process_file()