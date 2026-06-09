import secrets
import string
import tkinter as tk
from tkinter import messagebox


# --- LÓGICA DO GERADOR DE SENHAS ---
def gerar_senha_forte(comprimento=16, incluir_simbolos=True):
    letras = string.ascii_letters
    digitos = string.digits
    simbolos = string.punctuation

    caracteres_permitidos = letras + digitos
    if incluir_simbolos:
        caracteres_permitidos += simbolos

    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits)
    ]
    if incluir_simbolos:
        senha.append(secrets.choice(simbolos))

    comprimento_restante = comprimento - len(senha)
    senha += [secrets.choice(caracteres_permitidos) for _ in range(comprimento_restante)]

    senha_final = []
    while senha:
        caractere = secrets.choice(senha)
        senha_final.append(caractere)
        senha.remove(caractere)

    return "".join(senha_final)


# --- FUNÇÕES DA INTERFACE ---
def acao_gerar_senha():
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento < 8:
            messagebox.showwarning("Aviso", "Para sua segurança, use no mínimo 8 caracteres.")
            return

        incluir_simbolos = var_simbolos.get()
        nova_senha = gerar_senha_forte(comprimento, incluir_simbolos)

        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, nova_senha)
        entry_resultado.config(state="readonly")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido para o comprimento.")


def acao_copiar():
    senha = entry_resultado.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro para poder copiar.")


# --- PALETA DE CORES (FUNDO AZUL BEBÊ + DETALHES EM ROSA) ---
COR_AZUL_BEBE = "#d4f0ff"  # Fundo da tela inteira
COR_ROSA_PRINCIPAL = "#ff8da1"  # Rosa marcante para o botão principal
COR_ROSA_ESCURO = "#d65a7f"  # Um tom de rosa mais escuro para o título e textos importantes
COR_CAIXA_TEXTO = "#ffffff"  # Branco puro para os fundos dos campos (garante excelente leitura)
COR_TEXTO_ESCURO = "#2c3e50"  # Azul escuro/cinza para os textos secundários

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("420x340")
janela.resizable(False, False)
janela.configure(bg=COR_AZUL_BEBE)  # Define o fundo Azul Bebê

# 1. Título do App (Em Rosa Escuro para dar contraste)
lbl_titulo = tk.Label(janela, text="Gerador de Senhas", font=("Segoe UI", 16, "bold"), bg=COR_AZUL_BEBE,
                      fg=COR_ROSA_ESCURO)
lbl_titulo.pack(pady=(20, 10))

# 2. Componente para o Comprimento da Senha
lbl_comprimento = tk.Label(janela, text="Comprimento da Senha (Mínimo 8):", font=("Segoe UI", 10, "bold"),
                           bg=COR_AZUL_BEBE, fg=COR_TEXTO_ESCURO)
lbl_comprimento.pack(pady=(10, 0))

entry_comprimento = tk.Entry(janela, font=("Segoe UI", 11), justify="center", width=6, bg=COR_CAIXA_TEXTO,
                             fg=COR_TEXTO_ESCURO, insertbackground=COR_TEXTO_ESCURO, relief="flat")
entry_comprimento.insert(0, "16")
entry_comprimento.pack(pady=5)

# 3. Componente (Checkbox) para Símbolos
var_simbolos = tk.BooleanVar(value=True)
chk_simbolos = tk.Checkbutton(
    janela, text="Incluir Símbolos (!@#$)", variable=var_simbolos,
    font=("Segoe UI", 10, "bold"), bg=COR_AZUL_BEBE, fg=COR_TEXTO_ESCURO,
    activebackground=COR_AZUL_BEBE, activeforeground=COR_ROSA_ESCURO, selectcolor=COR_CAIXA_TEXTO
)
chk_simbolos.pack(pady=5)

# 4. Botão para Gerar (Botão Rosa com texto branco)
btn_gerar = tk.Button(
    janela, text="GERAR SENHA", command=acao_gerar_senha,
    bg=COR_ROSA_PRINCIPAL, fg="white", font=("Segoe UI", 10, "bold"),
    width=18, relief="flat", activebackground="#ff738c"
)
btn_gerar.pack(pady=15)

# 5. Campo para Exibir a Senha Gerada (Texto em Rosa Escuro no fundo Branco)
entry_resultado = tk.Entry(
    janela, font=("Consolas", 13, "bold"), justify="center", width=30,
    bg=COR_CAIXA_TEXTO, fg=COR_ROSA_ESCURO, relief="flat", readonlybackground=COR_CAIXA_TEXTO
)
entry_resultado.config(state="readonly")
entry_resultado.pack(pady=5)

# 6. Botão para Copiar a Senha (Fundo Branco com letras em Rosa)
btn_copiar = tk.Button(
    janela, text="Copiar Senha", command=acao_copiar,
    bg=COR_CAIXA_TEXTO, fg=COR_ROSA_ESCURO, font=("Segoe UI", 10, "bold"),
    width=18, relief="flat", activebackground="#f0f0f0"
)
btn_copiar.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()

# Atualizando o grafico
