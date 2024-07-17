#####################################################################################################
##          Codigo feito por Joao Victor A. P. (joaovictorpimenta@gmail.com/@joao_vap)             ##
##                                                                                                 ##
##         --> Inspirado e possibilitado pela divulgadora Julia Marcolan (@julhamarcolan)          ##
#####################################################################################################

import sys
import numpy as np
import matplotlib.pyplot as plt


argumentos = sys.argv

# argumentos[0] nome desse arquivo
# argumentos[1] nome do arquivo que contém os valores
 
npontos = argumentos[1].split("-")[1][1:]


## "pot" vai definir o contraste nas imagens a serem criadas [0 < pot <= 1]
pot = [0.2, 0.4, 0.6, 0.8]

## Deixamos a escolha basica de cores a cargo de quem roda o programa
cmap = input("cmap:")

if cmap == "":
    cmap = "inferno"
for p in pot:
    ## Carrega-se o texto do outro arquivo
    imagem = (np.loadtxt(argumentos[1]) + 1)**p

    ## Resta definir as cores e abrir a imagem
    try: 
        plt.imshow(imagem, cmap=cmap)
    except ValueError:
        cmap = "inferno"
        plt.imshow(imagem, cmap=cmap)        
    plt.savefig('{}-npontos.{}.resolucao.1024x1024'.format(cmap,npontos) + '_p.' + str(p) + '.png')
