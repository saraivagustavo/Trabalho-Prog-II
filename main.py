#Grupo: Gustavo Saraiva Mariano; Pedro Henrique Albani Nunes


######################################################################################################################################
#FUNÇÕES AUXILIARES GLOBAIS
def f_Ordenacao(dicionario):
    l = []
    for chave in dicionario:
        l.append(chave)
    f_quickSort(l, dicionario)
    return l

######################################################################################################################################


######################################################################################################################################
#FUNÇÕES AUXILIARES DA PRIMEIRA PARTE DO TRABALHO   
def f_formatarData(data): # função auxiliar para formatar a saída da data de acordo com o solicitado
    dia, mes, ano, hora, minuto = data
    return f'{dia}/{mes}/{ano} {hora}:{minuto}'

def f_quickSort(l, dicionario, inicio=0, fim=None):
    if fim is None:
        fim = len(l) - 1
    if inicio < fim:
        pivo = f_particao(l, dicionario, inicio, fim)
        f_quickSort(l, dicionario, inicio, pivo - 1)
        f_quickSort(l, dicionario, pivo + 1, fim)

def f_particao(l, dicionario, inicio, fim):
    i = inicio - 1
    pivo = l[fim]
    for j in range(inicio, fim):
        if len(dicionario[l[j]][1]) > len(dicionario[pivo][1]): # comparar por quem segue mais pessoas
            i += 1
            l[i], l[j] = l[j], l[i]
        elif len(dicionario[l[j]][1]) == len(dicionario[pivo][1]) and len(dicionario[l[j]][2]) > len(dicionario[pivo][2]):
            i += 1
            l[i], l[j] = l[j], l[i]
        elif len(dicionario[l[j]][1]) == len(dicionario[pivo][1]) and len(dicionario[l[j]][2]) == len(dicionario[pivo][2]) and dicionario[l[j]][0] < dicionario[pivo][0]:
            i += 1
            l[i], l[j] = l[j], l[i]
        elif len(dicionario[l[j]][1]) == len(dicionario[pivo][1]) and len(dicionario[l[j]][2]) == len(dicionario[pivo][2]) and dicionario[l[j]][0] == dicionario[pivo][0] and l[j] < pivo:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i + 1], l[fim] = l[fim], l[i + 1]
    return i + 1

################################################ PRIMEIRA PARTE DO TRABALHO ##########################################################
def f_usuarios(l, dicionario, saidas): # função para a primeira saída, relação das contas que o usuário segue a os seus seguidores
    with open(saidas, 'a') as f:
        for login in l:
            f.write(f'{dicionario[login][0]} (segue {len(dicionario[login][1])}, seguido por {len(dicionario[login][2])})\n')
        f.write('---\n')
######################################################################################################################################



######################################################################################################################################
#FUNÇÕES AUXILIARES PARA A SEGUNDA PARTE DO TRABALHO
def f_maiorFeed(n, pivo): # Função para verificar os primeiros posts do feed
    dia1, mes1, ano1, hora1, min1 = pivo[2]
    dia2, mes2, ano2, hora2, min2 = n[2]

    if ano2 < ano1: return True
    if ano2 > ano1: return False

    if mes2 < mes1: return True
    if mes2 > mes1: return False

    if dia2 < dia1: return True
    if dia2 > dia1: return False

    horarioTotal1 = (hora1 * 60) + min1
    horarioTotal2 = (hora2 * 60) + min2

    if horarioTotal2 < horarioTotal1: return True
    if horarioTotal2 > horarioTotal1: return False

    return n[1] > pivo[1]

def f_particao2(l, inicio, fim): # Função para fazer a partição da segunda parte do trabalho
    pivo = l[inicio]
    i = inicio + 1
    j = fim
    while i <= j:
        while i <= j and not f_maiorFeed(l[i], pivo):
            i += 1
        while j >= i and f_maiorFeed(l[j], pivo):
            j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
    l[inicio], l[j] = l[j], l[inicio]
    return j

def f_quickSort2(l, inicio, fim):
    if inicio < fim:
        pivo = f_particao2(l, inicio, fim)
        f_quickSort2(l, inicio, pivo - 1)
        f_quickSort2(l, pivo + 1, fim)

################################################ SEGUNDA PARTE DO TRABALHO ##########################################################
def f_feedUsuarios(dicionario, saidas): # função que printa todo o feed do usuário de acordo com as informações fornecidas no dicionário
    usuariosOrdenados = f_Ordenacao(dicionario)
    chave = usuariosOrdenados[0]
    with open(saidas, 'a') as f:
        f.write(f'Feed de {dicionario[chave][0]}\n')
        f.write('***\n')
        f_buscaFeed(chave, dicionario, f)

def f_buscaFeed(chave, dicionario, f): # função para buscar os seguidos de cada usuário
    l = []
    for pessoaSeguindo in dicionario[chave][1]:  # Lista de pessoas que o usuário está seguindo
        for nomeFoto, legenda, data in dicionario[pessoaSeguindo][3]:
            l.append((nomeFoto, legenda, data, pessoaSeguindo))  # Adiciona também a pessoa que postou
    f_quickSort2(l, 0, len(l) - 1)  # Ordena a lista fora do loop
    for nomeFoto, legenda, data, pessoaSeguindo in l:
        f.write(f'{pessoaSeguindo}\n')
        f.write(f'{nomeFoto}\n')
        f.write(f'{legenda}\n')
        f.write(f'{f_formatarData(data)}\n')
        f.write('***\n')

######################################################################################################################################

########################################################### MAIN #####################################################################
def main(args):
    import pickle
    import time
    inicio = time.time()
    saidas = 'saida.txt'
    with open(saidas, 'w') as f:  # Limpa o conteúdo anterior do arquivo de saída
        f.write('')
    with open('usuarios.bin', 'rb') as arquivo:
        dicionario = pickle.load(arquivo)
        l = f_Ordenacao(dicionario)
        f_usuarios(l, dicionario, saidas)
        f_feedUsuarios(dicionario, saidas)
    fim = time.time()
    tempo = fim - inicio
    print(f'{tempo:.2f}')
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))