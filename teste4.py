import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_valor():
    try:
        # Obter o valor da parcela e substituir a vírgula por ponto
        valor_parcela = float(entry_valor_parcela.get().replace(',', '.'))
        
        # Obter as datas
        data_vencimento = datetime.strptime(entry_data_vencimento.get(), '%d/%m/%Y')
        data_pagamento = datetime.strptime(entry_data_pagamento.get(), '%d/%m/%Y')
        
        # Valores fixos
        multa_percentual = 2  # Multa de 2%
        taxa_reemissao_boleto = 2.88
        
        # Cálculo dos dias de atraso
        dias_diferenca = (data_pagamento - data_vencimento).days
        
        # Cálculo das multas
        multa_por_atraso = (multa_percentual / 100) * valor_parcela
        multa_dias_atraso = (multa_por_atraso / 30) * dias_diferenca if dias_diferenca > 0 else 0
        
        # Cálculo do valor total
        valor_total = valor_parcela + multa_por_atraso + multa_dias_atraso + taxa_reemissao_boleto
        
        # Formatando o resultado para exibição
        resultado = (
            f"\nResumo do Pagamento:\n"
            f"\nValor da Parcela: R$ {valor_parcela:.2f}\n"
            f"Dias de Atraso: {dias_diferenca} dias\n"
            f"Multa por Atraso: R$ {multa_por_atraso:.2f}\n"
            f"Multa por Dias de Atraso: R$ {multa_dias_atraso:.2f}\n"
            f"Taxa de Reemissão de Boleto: R$ {taxa_reemissao_boleto:.2f}\n"
            f"\nValor Total a Pagar: R$ {valor_total:.2f}"
        )
        
        result_text.set(resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def format_date(event):
    """ Formata a data enquanto o usuário digita """
    widget = event.widget
    text = widget.get()
    
    # Se o texto tiver comprimento 2 ou 5, insere uma barra '/'
    if len(text) in [2, 5] and text[-1] != '/':
        widget.insert(tk.END, '/')

# Configuração da janela principal
root = tk.Tk()
root.title("Cálculo de Multa e Atraso - Made By Vitão")
root.configure(bg='#f0f0f0')

# Estilo das fontes
font_title = ('Helvetica', 14, 'bold')
font_label = ('Helvetica', 12)
font_entry = ('Helvetica', 12)
font_result = ('Helvetica', 12)

# Frame principal
frame = tk.Frame(root, padx=20, pady=20, bg='#f0f0f0')
frame.pack(padx=10, pady=10)

# Título
tk.Label(frame, text="Cálculadora de Multa por Atraso", font=font_title, bg='#f0f0f0').grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Labels e entradas
tk.Label(frame, text="Valor da Parcela:", font=font_label, bg='#f0f0f0').grid(row=1, column=0, sticky='e', pady=5)
entry_valor_parcela = tk.Entry(frame, font=font_entry)
entry_valor_parcela.grid(row=1, column=1, pady=5, padx=10)

tk.Label(frame, text="Data de Vencimento (dd/mm/aaaa):", font=font_label, bg='#f0f0f0').grid(row=2, column=0, sticky='e', pady=5)
entry_data_vencimento = tk.Entry(frame, font=font_entry)
entry_data_vencimento.grid(row=2, column=1, pady=5, padx=10)
entry_data_vencimento.bind('<KeyRelease>', format_date)

tk.Label(frame, text="Data de Pagamento (dd/mm/aaaa):", font=font_label, bg='#f0f0f0').grid(row=3, column=0, sticky='e', pady=5)
entry_data_pagamento = tk.Entry(frame, font=font_entry)
entry_data_pagamento.grid(row=3, column=1, pady=5, padx=10)
entry_data_pagamento.bind('<KeyRelease>', format_date)

# Botão para calcular
btn_calcular = tk.Button(frame, text="Cálcular", command=calcular_valor, font=font_label, bg='#4CAF50', fg='white', padx=10, pady=5, relief='flat')
btn_calcular.grid(row=4, column=0, columnspan=2, pady=20)

# Resultado
result_text = tk.StringVar()
tk.Label(frame, textvariable=result_text, font=font_result, bg='#f0f0f0', justify="left").grid(row=5, column=0, columnspan=2)

# Loop principal da interface
root.mainloop()
