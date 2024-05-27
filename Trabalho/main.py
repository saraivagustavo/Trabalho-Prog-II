def f_usuarios(dicionario): #função para a primeira saída, relação das contas que o usuário segue a os seus seguidores
        for chave in dicionario:
            print(f'{dicionario[chave][0]} (segue {len(dicionario[chave][1])}, seguido por {len(dicionario[chave][2])})')
        print('---')


'''def f_posts(dicionario):
    for chave in dicionario:
        for nome, legenda, data in dicionario[chave][3]:
            print(f'{chave}')
            print(f'{nome}')
            print(f'{legenda}')
            f_formatarData(data)
            print('***')'''

def f_formatarData(data): #função auxiliar para formatar a saída da data de acordo com o solicitado
    dia,mes,ano,hora,minuto = data
    print(f'{dia}/{mes}/{ano} {hora}:{minuto}')



def f_feedUsuarios(dicionario): #função que printa todo o feed do usuário de acordo com as informações fornecidas no dicionários
    for chave in dicionario:
        print(f'Feed de {dicionario[chave][0]}')
        print('***')
        for nome, legenda, data in dicionario[chave][3]:
            print(f'{chave}')
            print(f'{nome}')
            print(f'{legenda}')
            f_formatarData(data)
            print('***')



def main(args):
    import pickle
    with open('usuarios.bin', 'rb') as arquivo:
        dicionario = pickle.load(arquivo)
        #print(dicionario) #nome(chave): usuario dnv, lista com os nomes dos usuários que ele segue, lista com nome dos usuários que ele é seguido, depois vem a publicações nessa ordem: foto,legenda(opcional),data.   exemplo de publicação: ('foto0.jpg', 'Biscoito', (9, 6, 2023, 16, 30))
    f_usuarios(dicionario)
    f_feedUsuarios(dicionario)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
