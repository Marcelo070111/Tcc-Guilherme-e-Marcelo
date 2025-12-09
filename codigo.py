def saudacao_Gui(nome):
    import random 
    frases = [
        "Bom dia! Meu nome é " + nome + ". Como vai você?",
        "Olá!",
        "Oi, tudo bem?"
    ]
    return frases[random.randint(0,2)]



# NÃO USAMOS MAIS input(), então removido
def recebeTexto_GUI():
    pass



def buscaResposta_GUI(nome, texto):
    """
    Busca resposta no arquivo.
    Se não encontrar: retorna "DESCONHECIDO"
    Assim o GUI trata o caso e pede sugestão ao usuário.
    """

    texto_limpo = texto.strip()

    with open("ChatBotTreino.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)

        while True:
            linha = conhecimento.readline()

            if linha != "":
                # Se o usuário disse tchau
                if texto_limpo.replace("Cliente: ", "") == "Tchau":
                    return "FIM"

                # Se encontrou a pergunta no arquivo
                if linha.strip() == texto_limpo:
                    prox = conhecimento.readline()
                    if prox.startswith("Chatbot:"):
                        return prox.replace("Chatbot: ", "").strip()
            else:
                # Se chegou ao fim do arquivo e não achou resposta
                conhecimento.write("\n" + texto_limpo)
                return "DESCONHECIDO"



def exibeResposta_GUI(texto_usuario, resposta, nome):
    """
    Formata a resposta para exibir na interface.
    """

    if resposta == "FIM":
        return f"{nome}: volte sempre!"

    return f"{nome}: {resposta}"



def salva_sugestao(sugestao):
    """
    Salva a sugestão dada pelo usuário como nova resposta do Chatbot.
    """
    with open("ChatBotTreino.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.write("\nChatbot: " + sugestao + "\n")



# Jaccard permanece igual
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum / (len(textoBase.split()))


def limpa_frase(frase):
    tirar = ["?","!","...",".",",","\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase
