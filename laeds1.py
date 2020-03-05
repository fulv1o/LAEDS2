"""
Exercício 1 de LAEDs
Aluno: Fúlvio Taroni Monteforte
"""
def indice_prim_valor_igual(lista1, lista2):
    """
    @Autor: Fúlvio Taroni Monteforte
    Retorna o índice da lista1 onde ocorre a primeira repetição de um valor na lista 2
    :param lista1: 'Lista 1'
    :param lista2: 'Lista 2'
    :return: 'Índice da repetição'
    """
    i = 0
    for num in lista1:
        if num in lista2:
            return i
        i += 1
    return -1

def valores_iguais(lista1, lista2):
    """
    @Autor: Fúlvio Taroni Monteforte
    Cria uma lista contendo os valores iguais entre duas listas passadas como parâmetro
    :param lista1: 'Lista 1'
    :param lista2: 'Lista 2'
    :return: 'Lista contendo os valores repetidos'
    """
    lista3 = list()

    for num in lista1:
        if num in lista2:
            lista3.append(num)

    return lista3


def media(lista):
    """
    @Autor: Fúlvio Taroni Monteforte
    Calcula a média dos valores de uma lista
    :param lista: 'lista com os valores'
    :return: 'resultado da média'
    """
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]

    return resultado/len(lista)


def soma(lista, x=0):
    """
    @Autor: Fúlvio Taroni Monteforte
    Faz a soma dos itens de uma lista e possivelmente soma um parâmetro X
    :param lista: 'Espera receber uma lista com valores'
    :param x: 'Valor opcional'
    :return: 'Resultado da soma de todos os valores'
    """
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]

    return resultado + x

def maior(a,b):
    """
    @Autor: Fúlvio Taroni Monteforte
    Descobre o maior valor entre dois números
    :param a: 'Número 1'
    :param b: 'Número 2'
    :return: 'Maior valo'
    """
    if a == b:
        return "Os valores são iguais"
    elif a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    x = maior(2, 3)
    print(f"Maior = {x}")

    y = soma([2, 3, 5, 6])
    print(f'Soma = {y}')

    w = media([14, 16, 1, 0, 2, 3, 7, 1])
    print(f'Media = {w}')

    z = valores_iguais([1, 2, 3, 4, 5], [4, 5, 6, 7])
    print(f'Valores iguais: {z}')

    a = indice_prim_valor_igual([1, 2, 3, 4], [0, 2, 4, 5])
    print(f'Índice da primeira repetição: {a}')

