import tkinter as tk

def clicar_botao(valor):
    entrada_atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, entrada_atual + valor)

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        expressao = visor.get()
        resultado = str(eval(expressao))
        visor.delete(0, tk.END)
        visor.insert(0, resultado)
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# JANELA
janela = tk.Tk()
janela.title("Calculadora Visual")
janela.geometry("300x400")
janela.resizable(False, False)

# VISOR
visor = tk.Entry(janela, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
visor.grid(row=0, column=0, columnspan=4, pady=10)

# BOTÕES
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# ADICONANDO BOTÕES
for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, font=("Arial", 16), bg="lightblue", fg="black",
                          command=calcular)
        botao.grid(row=linha, column=coluna, columnspan=4, sticky="nsew", padx=5, pady=5)
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, font=("Arial", 16), bg="lightcoral", fg="black",
                          command=limpar)
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)
    else:
        botao = tk.Button(janela, text=texto, font=("Arial", 16), bg="lightgray", fg="black",
                          command=lambda valor=texto: clicar_botao(valor))
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):
    janela.grid_columnconfigure(j, weight=1)

if __name__ == '__main__':
    janela.mainloop()