def saudacao_Gui(nome):
    import random 
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    return frases[random.randint(0,2)]

def recebeTexto_GUI():
    texto = "Cliente:" + input("Cliente")
    palavraProibida = ["bocó"]
    for p in palavraProibida:
        if p in texto:
            print("Não vem não! Me respeite!")
            return recebeTexto_GUI()
        return texto 

def buscaResposta_GUI(nome,texto):
    with open("ChatBotTreino.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ","") == "Tchau":
                    print(nome+ ": volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha 
            else:
                print("Me desculpe, não sei oque falar")
                conhecimento.write("\n" + texto)
                resposta_user = input("Oque esperava?\n")
                conhecimento.write ("\n" +"Chatbot: "+resposta_user)
                return "Hum..."

def exibeResposta_GUI(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == "fim":
        return "fim"
    return "Continua"    

def salva_sugestao(sugestao):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")
    
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase 