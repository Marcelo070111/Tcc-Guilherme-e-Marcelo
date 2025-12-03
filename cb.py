import codigo as cb

nome_maquina = "Nelson bomerang"
cb.saudaçoes(nome_maquina)
while True:
    texto = cb.recebeTexto()
    resposta = cb.buscaResposta(nome_maquina, texto)
    if cb.exibeResposta(resposta, nome_maquina) == 'fim':
        break 