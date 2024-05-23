def f_usuarios(dicionario):
    for chave in dicionario:
        n = 0
        while len(dicionario) >= n:
            n += 1
        print(f'{dicionario[chave][0]} (segue {len(dicionario[chave][1])}, seguido por {len(dicionario[chave][2])})')
    print('---')




def main(args):
    import pickle
    arquivo_binario = 'usuarios.bin'

    with open(arquivo_binario, 'rb') as arquivo:
        dicionario = pickle.load(arquivo)
    #print(dicionario) #nome(chave): usuario dnv, lista com os nomes dos usuários que ele segue, lista com nome dos usuários que ele é seguido, depois vem a publicações nessa ordem: foto,legenda(opcional),data.
    f_usuarios(dicionario)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))