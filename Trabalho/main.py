''''FUNÇÕES AUXILIARES'''
def f_intercalar(l,lEsq,lDir):
    i = 0
    j = 0
    k = 0
    while(i < len(lEsq)) and (j < len(lDir)):
        if(lEsq[i] < lDir[j]):
            l[k] = lEsq[i]
            i += 1
        else:
            l[k] = lDir[j]
            j += 1
        k += 1
    while(i < len(lEsq)):
        l[k] = lEsq[i]
        i += 1
        k += 1
    while(j < len(lDir)):
        l[k] = lDir[j]
        j += 1
        k += 1

def f_mergeSort(l):
    if(len(l) <= 1):
        return l
    else:
        meio = len(l) // 2
        lEsq = l[:meio] #não pega o meio
        lDir = l[meio:] #pega o meio
        f_mergeSort(lEsq)
        f_mergeSort(lDir)
        f_intercalar(l,lEsq,lDir)
        return l
    


'''def f_definirMaior(dicionario,chave):
    for comparar in dicionario:
        if comparar != chave:
            f_maior(len(dicionario[chave][2]), len(dicionario[comparar][2]))
    
def f_maior(x,y):
    if x < y:
        return True
    if y < x:
        return False'''
    

def f_formatarData(data): #função auxiliar para formatar a saída da data de acordo com o solicitado
    dia,mes,ano,hora,minuto = data
    print(f'{dia}/{mes}/{ano} {hora}:{minuto}')


def f_buscaFeed(chave, dicionario): #função para buscar os seguidos de cada usuário
    for pessoaSeguindo in dicionario[chave][1]:
        for nome, legenda, data in dicionario[pessoaSeguindo][3]:
            print(f'{pessoaSeguindo}')
            print(f'{nome}')
            print(f'{legenda}')
            f_formatarData(data)
            print('***')



'''PRIMEIRA PARTE DO TRABALHO'''
def f_usuarios(dicionario): #função para a primeira saída, relação das contas que o usuário segue a os seus seguidores
        l = []
        for chave in dicionario:
                print(f'{dicionario[chave][0]} (segue {len(dicionario[chave][1])}, seguido por {len(dicionario[chave][2])})')
        print('---')

'''SEGUNDA PARTE DO TRABALHO'''
def f_feedUsuarios(dicionario): #função que printa todo o feed do usuário de acordo com as informações fornecidas no dicionários
    for chave in dicionario:
        print(f'Feed de {dicionario[chave][0]}')
        print('***')
        f_buscaFeed(chave,dicionario)



def main(args):
    import pickle
    with open('usuarios.bin', 'rb') as arquivo:
        dicionario = pickle.load(arquivo)
        #nome.sobrenome(chave): nome do usuário por extenso "Pedro Oliveira", lista com os nomes dos usuários que ele segue, lista com nome dos usuários que ele é seguido, 
        #depois vem a publicações nessa ordem: foto,legenda(opcional),data.   exemplo de publicação: ('foto0.jpg', 'Biscoito', (9, 6, 2023, 16, 30))
    #print(dicionario)
    #f_feedUsuarios(dicionario)
    f_usuarios(dicionario)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
