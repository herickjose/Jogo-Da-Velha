import random
from os import system, name

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2020102393" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "HERICK JOSE DE ALBUQUERQUE CORREIA" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear')

def soliciteLetra():
    """
    Essa função solicita do usuário (no caso, o jogador) que ele escolha uma letra entre X ou O, onde, o retorno será
    atribuído a duas variaveis, uma para o Jogador e outra para o Computador/PC.
    """
    letra = input("Você deseja ser X ou O? ")
    #Está parte verifica se as duas escolhas do input foram satisfeitas, caso contrário será solicitado novamente
    #a escolha da letra.
    if letra != "X" and letra != "O":
        print(f'Opção inválida!')
        return soliciteLetra()
    elif letra == "X":
        print(f'Jogador é {letra} e PC é O.')
        return "X", "O" #a primeira string será direcionada ao Jogador e a segunda ao Computador.
    else:
        print(f'Jogador é {letra} e PC é X.')
        return "O", "X" #a primeira string será direcionada ao Jogador e a segunda ao Computador.

def primeiraJogada():
    """
    Essa função usa uma lista para escolher qual letra que irá começar a partida do Jogo da Velha, onde,
    o retorno será atribuído a uma variável na função main.
    """
    listaTeste = ["X", "O", "X", "O"] #lista necessária para ser escolhida aleatoriamente quem irá começar.
    teste = random.choice(listaTeste) #variavel que utiliza de Random para fazer uma escolha aleatória da lista.
    return teste

def imprimeTabuleiro(tabuleiro):
    """
    Essa função imprime o tabuleiro e utiliza de uma lista com 10 indices para elabora-lá. Não retorna nada, somente imprime.
    Onde a sequência do tabuleiro está de acordo com o teclado númerico.
    """
    print(" "+tabuleiro[7]+" | "+tabuleiro[8]+" | "+tabuleiro[9])
    print("---+---+---")
    print(" "+tabuleiro[4]+" | "+tabuleiro[5]+" | "+tabuleiro[6])
    print("---+---+---")
    print(" "+tabuleiro[1]+" | "+tabuleiro[2]+" | "+tabuleiro[3])


def jogadaHumano(tabuleiro, simboloJogador):
    """
    Essa função que será responsável por elaborar a jogada do Jogador, onde, ela utiliza do tabuleiro(no caso, a lista com 10 indices),
    e o simbolo que identifica quem é o jogador. Ela retornará o tabuleiro modificado pela posição que será escolhida pelo Jogador.
    """
    #Parte inicial, onde é solicitado a escolha de uma posição para o jogador, onde os números selecionados serão avalidados.
    posicao = int(input("Escolha uma posição de 1 a 9: "))
    #Este if é para verificar se a escolha de posição está de acordo com o tamanho do tabuleiro, caso não esteja será solicitado
    #novamente a posição que o mesmo deseja escolher.
    if posicao != 1 and posicao != 2 and posicao != 3 and posicao != 4 and posicao != 5 and posicao != 6 and posicao != 7 and posicao != 8 and posicao != 9:
        print(f'Valor inválido!')
        return jogadaHumano(tabuleiro, simboloJogador)
    #este elif verifica se a posição está vazia, se estiver, ele irá ocupar a posição do tabuleiro com o simbolo do Jogador.
    elif tabuleiro[posicao] == " ":
        tabuleiro[posicao] = simboloJogador
        return tabuleiro #este return é o que irá mudar o tabuleiro de acordo com o simbolo e a posição escolhida pelo jogador.
    else:
        #este else serve para chamar a função novamente caso a posição esteja ocupada.
        print(f'Posição já ocupada!')
        return jogadaHumano(tabuleiro, simboloJogador)

def verificaVitoria(tabuleiro, letra):
    """
    Essa função utiliza do tabuleiro e da letra do Jogador ou do Computador para fazer as seguintes verificações:
    1° Verifica cada linha;
    2° Verifica cada coluna;
    3° Verifica cada diagonal;
    Retornando então o resultado como True se as condições forem verdadeiras e False se acontecer algum equivoco nas
    sequências de verificação.
    """
    resultado = False
    #verificando linha
    if tabuleiro[7] == letra and tabuleiro[8] == letra and tabuleiro[9] == letra:
        resultado = True
    elif tabuleiro[4] == letra and tabuleiro[5] == letra and tabuleiro[6] == letra:
        resultado = True
    elif tabuleiro[1] == letra and tabuleiro[2] == letra and tabuleiro[3] == letra:
        resultado = True
    #verificando coluna
    elif tabuleiro[7] == letra and tabuleiro[4] == letra and tabuleiro[1] == letra:
        resultado = True
    elif tabuleiro[8] == letra and tabuleiro[5] == letra and tabuleiro[2] == letra:
        resultado = True
    elif tabuleiro[9] == letra and tabuleiro[6] == letra and tabuleiro[3] == letra:
        resultado = True
    #verificando diagonal
    elif tabuleiro[7] == letra and tabuleiro[5] == letra and tabuleiro[3] == letra:
        resultado = True
    elif tabuleiro[1] == letra and tabuleiro[5] == letra and tabuleiro[9] == letra:
        resultado = True
    return resultado


def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador:

    Bom, minha estrategia foi da seguinte forma, se nas pontas dos cantos tiverem preenchidas pelo simbolo do Computador,
    ele irá completar o meio entre esses dois simbolos que o representa. Ex: Se o computador começar, ele irá escolher umas
    das seguintes posições 1 ou 3 ou 7, assim, quando o Humano perceber que pelo menos uma das duas posições estará preenchida
    pelo simbolo do Computador, obviamente, ele irá marcar a posição em que se o Computador marcar irá vencer o jogo, mas quando
    o Humano marcar naquela posição, logo, o Computador irá marcar a posição que fará com que ele ganhe de 3 formas, onde poderá
    ser pelo diagonal (7, 5 e 3) ou, pela coluna esquerda (7, 4, 1) ou pela parte inferior do tabuleiro (1, 2, 3), assim,
    não havendo forma de escapatória do oponente do computador. Podemos concluir que posso chamar de metodo do triângulo
    retângulo(kkkk, inventei esse nome, perdão). Esse metodo é aplicado de diversas formas, podendendo então variar de acordo
    com as posições solicitadas.
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9] #lista de escolha de posição aleatória.
    jogada = random.choice(l) #variavel responsavel por fazer a escolha aleatória de uma posição, utilizando uma lista.
    
    #verificando posições 1, 3 e 7
    if tabuleiro[l[0]] == " ":
        tabuleiro[l[0]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[2]] == " ":
        tabuleiro[l[2]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[6]] == " ":
        tabuleiro[l[6]] = simboloComputador
        return tabuleiro
    #verificando se pode completar uma das seguintes posições: 2, 4 e 5. Onde se for verificada e poder ser substituida pelo
    #simbolo do Computador, ele então irá vencer. 
    elif tabuleiro[l[0]] == simboloComputador and tabuleiro[l[2]] == simboloComputador and tabuleiro[l[1]] == " ":
        tabuleiro[l[1]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[0]] == simboloComputador and tabuleiro[l[6]] == simboloComputador and tabuleiro[l[3]] == " ":
        tabuleiro[l[3]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[6]] == simboloComputador and tabuleiro[l[2]] == simboloComputador and tabuleiro[l[4]] == " ":
        tabuleiro[l[4]] == simboloComputador
        return tabuleiro

    #verificando posições 1, 3 e 9
    elif tabuleiro[l[0]] == " ":
        tabuleiro[l[0]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[2]] == " ":
        tabuleiro[l[2]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[8]] == " ":
        tabuleiro[l[8]] = simboloComputador
        return tabuleiro
    #verificando se pode completar uma das seguintes posições: 2, 5 e 6. Onde se for verificada e poder ser substituida pelo
    #simbolo do Computador, ele então irá vencer.
    elif tabuleiro[l[0]] == simboloComputador and tabuleiro[l[2]] == simboloComputador and tabuleiro[l[1]] == " ":
        tabuleiro[l[1]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[2]] == simboloComputador and tabuleiro[l[8]] == simboloComputador and tabuleiro[l[5]] == " ":
        tabuleiro[l[5]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[0]] == simboloComputador and tabuleiro[l[8]] == simboloComputador and tabuleiro[l[4]] == " ":
        tabuleiro[l[4]] = simboloComputador
        return tabuleiro

    #verificando posições 7, 9 e 3
    elif tabuleiro[l[6]] == " ":
        tabuleiro[l[6]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[8]] == " ":
        tabuleiro[l[8]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[2]] == " ":
        tabuleiro[l[2]] = simboloComputador
        return tabuleiro
    #verificando se pode completar uma das seguintes posições: 8, 5 e 6. Onde se for verificada e poder ser substituida pelo
    #simbolo do Computador, ele então irá vencer.
    elif tabuleiro[l[6]] == simboloComputador and tabuleiro[l[8]] == simboloComputador and tabuleiro[l[7]] == " ":
        tabuleiro[l[7]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[8]] == simboloComputador and tabuleiro[l[2]] == simboloComputador and tabuleiro[l[5]] == " ":
        tabuleiro[l[5]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[6]] == simboloComputador and tabuleiro[l[2]] == simboloComputador and tabuleiro[l[4]] == " ":
        tabuleiro[l[4]] = simboloComputador
        return tabuleiro

    #verificando posições 9, 7 e 1
    elif tabuleiro[l[8]] == " ":
        tabuleiro[l[8]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[6]] == " ":
        tabuleiro[l[6]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[0]] == " ":
        tabuleiro[l[0]] = simboloComputador
        return tabuleiro
    #verificando se pode completar uma das seguintes posições: 8, 5 e 4. Onde se for verificada e poder ser substituida pelo
    #simbolo do Computador, ele então irá vencer.
    elif tabuleiro[l[8]] == simboloComputador and tabuleiro[l[6]] == simboloComputador and tabuleiro[l[7]] == " ":
        tabuleiro[l[7]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[6]] == simboloComputador and tabuleiro[l[0]] == simboloComputador and tabuleiro[l[3]] == " ":
        tabuleiro[l[3]] = simboloComputador
        return tabuleiro
    elif tabuleiro[l[8]] == simboloComputador and tabuleiro[l[0]] == simboloComputador and tabuleiro[l[4]] == " ":
        tabuleiro[l[4]] = simboloComputador
        return tabuleiro
    else:
        #Esse if somente será usado quando nenhuma das situações acima forem realizadas, então, ele irá sortear uma posição
        #aleatória.
        if tabuleiro[jogada] == " ":
            tabuleiro[jogada] = simboloComputador
            return tabuleiro
        else:
            #Caso a posição aleatória for uma posição já preenchida, ele irá chamar a função novamente para verificar e sortear
            #uma posição diferente, onde que ele repetirá até ser atendida a condição de parada.
            return jogadaComputador(tabuleiro, simboloComputador)

def jogoDaVelha(turno, tabuleiro, simboloJogador, simboloComputador, numJogadas = 1):
    """
    Essa função que é responsável por realizar tudo que o jogo precisa, utilizando então das funções que definimos antes.
    Onde ele usa a variável turno que representará a vez de quem irá escolher uma posição, a função usa também o tabuleiro que
    é a lista de 10 espaços vazios, onde a mesma será modificada ao decorrer do jogo, usa também o simbolo do Jogador e o
    simbolo do Computador e, por último, sendo uma das partes importantes que é a variável numJogadas que representa quantas
    jogadas(ou seja, quantas rodadas) já foram efetuadas, onde que esse valor decidirá se irá ocorrer empate ou não. 
    """
    print("--------------------------------")
    print(f"Numero de jogadas: {numJogadas}")#Imprime o número da rodada.
    print("--------------------------------")
    if turno == simboloJogador: #Se for a vez do Jogador.
        #então, ele verificará a posição selecionada, chamando a função jogadaHumano e irá imprimir o tabuleiro.
        tabuleiro = jogadaHumano(tabuleiro, simboloJogador)
        imprimeTabuleiro(tabuleiro)
        if verificaVitoria(tabuleiro, simboloJogador):
            #Está condição verificará se o Jogador vencerá a partida.
            print('-------------')
            print(f'Você venceu!')
            print('-------------')
            print()
            x = input("--> Aperte Enter para sair do game...")
            exit()
        elif numJogadas < 9: #Se nao empatou, ou seja, se o limite de rodadas foi alcançado, iremos chamar a vez do Computador.
            return jogoDaVelha(simboloComputador, tabuleiro, simboloJogador, simboloComputador, numJogadas + 1)
        else:
            #Este else que irá nos dizer o empate, pois se a condição acima não for satisfeita, então somente haverá uma solução
            #que é o empate. Então ele irá imprimir uma mensagem avisando.
            print('-------------')
            print(f'Deu velha!!!')
            print('-------------')
            x = input("--> Aperte Enter para sair do game...")
            exit()
    elif turno == simboloComputador: #se for a vez do Computador.
        #então, ele verificará a posição selecionada, chamando a função jogadaComputador e irá imprimir o tabuleiro.
        tabuleiro = jogadaComputador(tabuleiro, simboloComputador)
        imprimeTabuleiro(tabuleiro)
        if verificaVitoria(tabuleiro, simboloComputador):
            #Está condição verificará se o Computador vencerá a partida.
            print('---------------------')
            print(f"O computador venceu!")
            print('---------------------')
            print()
            x = input("--> Aperte Enter para sair do game...")
            exit(0)
        elif numJogadas < 9: #Se nao empatou, ou seja, se o limite de rodadas não foi alcançado, iremos chamar a vez do Jogador.
            return jogoDaVelha(simboloJogador, tabuleiro, simboloJogador, simboloComputador, numJogadas + 1)
        else:
            #Este else que irá nos dizer o empate, pois se a condição acima não for satisfeita, então somente haverá uma solução
            #que é o empate. Então ele irá imprimir uma mensagem avisando.
            print('-------------')
            print(f"Deu velha!!!")
            print('-------------')
            print()
            x = input("--> Aperte Enter para sair do game...")
            exit()

def main():
    limpaTela()
    M = getMatricula()
    N = getNome()
    print(f'Número de Matrícula: {M}') 
    print()
    print(f'Nome do Aluno: {N}')
    print()
    print(f"Seja bem-vindo ao Jogo da Velha! Boa sorte!")
    tab = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] #Lista fundamental para a realização de todo o jogo.
    imprimeTabuleiro(tab)#Chamada da função para imprimir o tabuleiro.

    jogador, PC = soliciteLetra()#Chamada da função para atribuir os resultados dos returns as duas variaveis, que são
    #o Jogador e o Computador.

    quemComeca = primeiraJogada()#Chamada da função que realiza a escolha de quem irá começar a partida do Jogo da Velha.
    if quemComeca == jogador:
        #Condições para imprimir que será que iniciará a partida.
        print('-----------------')
        print(f"O Humano começa!")
    else:
        print('---------------------')
        print(f'O computador começa!')

    jogoDaVelha(quemComeca, tab, jogador, PC)#Chamada da função principal, onde a mesma é responsavel por decidir o fluxo da partida.
    #onde as variaveis que definimos logo acima, aqui mesmo na função "def main()", serão utilizadas para o jogo fluir.


if __name__ == "__main__":
    main()