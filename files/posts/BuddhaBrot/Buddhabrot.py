#####################################################################################################
##          Codigo feito por Joao Victor A. P. (joaovictorpimenta@gmail.com/@joao_vap)             ##
##                                                                                                 ##
##         --> Inspirado e possibilitado pela divulgadora Julia Marcolan (@julhamarcolan)          ##
#####################################################################################################

import numpy as np
import random
import time

## Estabelecendo uma semente para resultados replicaveis
random.seed(314159)


def iteracoes(c):

    ## Vamos iniciar com z = (0, 0)
    z = complex(0, 0)
    i = 0

    ## Escape armazena os pontos registrados no processo, o 'caminho'
    escape = []

    while i < ciclos and abs(z * z + c) <= 2:

        ## Processo similar ao de Mandelbrot
        z = z * z + c

        ## Registra-se aqueles dentro da nossa janela de observaçao
        if b.real >= z.real >= a.real and b.imag >= z.imag >= a.imag:
            escape.append(z)

        i += 1

    return i, escape


def imagem(rx, ry, ie, sd):

    ## 'hx' e 'hy' sao as variacoes nas direcoes x e y considerando a resolucao
    hx = (sd.real - ie.real) / rx
    hy = (sd.imag - ie.imag) / ry

    ## matriz vai armazenar os elementos da nossa imagem
    ## preenche-se com zeros toda a matriz
    matriz = np.zeros((ry, rx))

    ## Para cada ponto, processa-se um ciclo
    j = 0
    while j in range(npontos):

        ## Definindo um ponto no espaço determinado
        ix, iy = random.randrange(0, rx), random.randrange(0, ry)
        x, y = ie.real + ix * hx, ie.imag + iy * hy
        ci = complex(x, y)

        ## Eliminando alguns numeros centrais no cardio principal
        if (ci.real + 0.2)**2 + ci.imag**2 <= 0.16:
            continue

        ## Para cada ponto, deve-se testar seu comportamento
        result = iteracoes(ci)

        ## Se o numero passou por todos os ciclos, exclui-se ele pois provavemente e de Mandelbrot
        if result[0] != ciclos:
            for elemento in result[1]:

                ## Descobrindo em qual elemento da matriz aloca-se o numero em questao
                indx = int(abs(elemento.real - ie.real)/hx)
                indy = int(abs(elemento.imag - ie.imag)/hy)

                ## Faz-se tambem o numero simetrico em relacao ao eixo imaginario para otimizaçao
                sindy = rx - indy - 1

                matriz[indx][indy] += 1
                matriz[indx][sindy] += 1

        j += 1

    ## Resta salvar o resultado em um arquivo de texto
    end = time.time()
    np.savetxt('saida-n{}-c{}.txt'.format(npontos, ciclos), np.matrix(matriz), fmt='%.0f')

    return end


## Esses parametros definem a regiao do plano complexo explorada
## "a" sendo o ponto inferior esquerdo do quadrado
## "b" sendo o ponto superior direito do quadrado
## "r" representa a 'resoluçao' que se quer a imagem nas duas direcoes

a = complex(-1.4, -1.4)
b = complex(1.4, 1.4)
r = [1024, 1024]

## Define-se a quantidade de pontos de usa para a execucao da imagem, 'npontos'
## Define-se a quantidade de ciclos do processo para cada ponto, 'ciclos'

npontos = int(input("Quantidade de pontos: "))
ciclos = int(input("Quantidade de ciclos: "))

## chama-se a funçao principal para criar o objeto com respectivos parametros

imagem(r[0], r[1], a, b)

