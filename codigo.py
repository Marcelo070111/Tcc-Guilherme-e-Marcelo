def saudaçoes(nome)
    import random 
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?," "Olá!," "Oi, tudo bem?"]
    print(frases[random.randit(0,2)])

def recebeTexto()
    texto = "Cliente:" + input("Cliente")
    palavraProibida = ["bocó"]
    for p in palavraProibida
        if p in texto:
            print("Não vem não! Me respeite!")
            return recebeTexto()
        return texto 

def buscaResposta(nome,texto):
    with open("ChatBotTreino.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while true:
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

def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == "fim":
        return "fim"
    return "Continua"    
