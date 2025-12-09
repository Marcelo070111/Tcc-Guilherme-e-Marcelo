import codigo as cb
from tkinter import *

main_window = Tk()
main_window.title("Chatbot")
main_window.geometry("500x700")

main_window.grid()

frame = Frame(main_window)
frame.grid()

l_identif = Label(frame, text="Insira uma mensagem: ")
l_identif.grid(row=0, column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)

Button(frame, text="Clique", command=lambda: roda_Chatbot()).grid(row=0, column=2)

frame2 = Frame(main_window)
frame2.grid(row=1, column=0)

# CAIXA DE TEXTO PARA MOSTRAR A CONVERSA
caixa = Text(frame2, height=30, width=50)
caixa.grid()

nome_maquina = "Nelson bomerang"
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""
historico_conversa = ""

# MOSTRA PRIMEIRA MENSAGEM
caixa.insert(END, "Qual seu nome?\n")

def atualizar_conversa():
    """Reescreve toda a conversa na caixa"""
    caixa.delete("1.0", END)
    caixa.insert(END, historico_conversa)

def roda_Chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario
    global nome_maquina

    texto = e_mensagem.get()

    if entrada_nome_usuario:
        nome_usuario = texto
        saudacao = cb.saudacao_Gui(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        entrada_nome_usuario = False

        atualizar_conversa()

    else:
        saudacao = cb.saudacao_Gui(nome_maquina)
        historico_conversa += "\n" + nome_usuario + ": " + texto

        if entrada_sugestao:
            cb.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\nAgora aprendi! Vamos continuar nossa conversa...\n"
            atualizar_conversa()

        else:
            resposta = cb.buscaResposta_GUI(nome_maquina, "Cliente: " + texto + "\n")

            if resposta == "Me desculpe, não sei oque falar":
                historico_conversa += "\nMe desculpe, não sei oque falar. O que você esperava?\n"
                entrada_sugestao = True
                atualizar_conversa()
            else:
                resposta_formatada = cb.exibeResposta_GUI(texto, resposta, nome_maquina)
                historico_conversa += "\n" + resposta_formatada
                atualizar_conversa()

    # Limpa o campo de digitação
    e_mensagem.delete(0, END)

main_window.mainloop()

