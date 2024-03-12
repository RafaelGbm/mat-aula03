import matplotlib.pyplot as plt
import numpy as np


# Função para visualização gráfica

'''
def plotar_funcao(func, x_range, titulo='', xlabel='x', ylabel='f(x)', legenda=''):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=legenda or titulo)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if legenda:
        plt.legend()
    plt.show()

# funções essenciais

def funcao_linear(x):
    return 2 * x + 3

#Plotando gráficos

plotar_funcao(funcao_linear, [-10, 10], "Função Linear", legenda= 'f(x)=2x + 3)')

#Exercício 01
# Dados do problema

anos = np.array([1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000])
percent_rural = np.array([30.4, 26.4, 23.6, 21.1, 19.0, 17.1, 15.0, 13.0, 11.7, 10.5])

#Ajustando Modelo Linear

coeficientes = np.polyfit(anos, percent_rural, 1)
modelo = np.poly1d(coeficientes)

estimativa_1988 = modelo (1988)
estimativa_2002 = modelo (2002)


plt.figure(figsize=(10, 6))
plt.plot(anos, percent_rural, 'o', label='Dados Originais')
plt.plot(anos, modelo(anos), 'r--', label=f'Modelo: {modelo}')
plt.title('Percentual da População Rural da Argentina (1955-2000)')
plt.xlabel('Ano')
plt.ylabel('% Rural')
plt.legend()
plt.grid(True)
plt.show()

(estimativa_1988, estimativa_2002)
'''
