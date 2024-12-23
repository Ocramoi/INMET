# n: número de observações;
# X: vetor de observações.
def media_aritmetica(n, X):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Inicia média aritmética:
    ma = 0

    # Para cada observação da variável aleatória X:
    for x in X:
        # Acumula:
        ma += x
    # Retorna a media aritmetica das observações de X:
    return (ma/n)

# k: número de observações distintas;
# N: vetor de números de repetições respectivas a cada observação distinta;
# X: vetor de observações distintas.
def media_aritmetica_de_observacoes_distintas_com_pesos_de_repeticao_associados(k, N, X):
    # Se número de observações distintas menor ou igual a zero:
    if k <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações distintas deve ser um natural não nulo.")

    # Inicia média aritmética:
    ma = 0
    # Inicia contador de número de observações total:
    n = 0

    # Para cada observação distinta:
    for i in range(0, k):
        # Se o número de observações de X[i] for menor que zero:
        if N[i] < 0:
            # Encerra o programa:
            raise Exception("Erro. O número de observações de um valor qualquer deve ser natural.")
        # Senão:
        else:
            # Acumula:
            ma += N[i]*X[i]
            # Incrementa o número de observações total:
            n += N[i] 
    
    # Se o número de observações total for igual a zero:
    if n == 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Senão:
    else:
        # Retorna a media aritmetica das observações de X:
        return (ma/n)
    
# Nota sobre a função acima: observe que estou flexibilizando a restrição dos valores de X
# serem distintos, e que a contagem de um valor qualquer pode ser zero (mas não todas elas). 

# k: número de observações distintas;
# F: vetor de frequências relativas a cada observação distinta;
# X: vetor de observações distintas.
def media_aritmetica_de_observacoes_distintas_com_frequencias_relativas_associadas(k, F, X):
    # Se número de observações distintas menor ou igual a zero:
    if k <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações distintas deve ser um natural não nulo.")

    # Inicia média aritmética:
    ma = 0
    # Inicia contador de frequência total:
    f = 0

    # Para cada observação distinta:
    for i in range(0, k):
        # Se a frequência relativa de X[i] for menor que zero:
        if F[i] < 0:
            # Encerra o programa:
            raise Exception("Erro. A frequência relativa de um valor qualquer deve ser um racional não negativo.")
        # Senão:
        else:
            # Acumula:
            ma += F[i]*X[i]
            # Incrementa a frequência total:
            f += F[i]
    
    # Se a frequência de observações total for diferente de 1:
    if f != 1:
        # Encerra o programa:
        raise Exception("Erro: a frequência não corresponde com o número de observações.")
    # Senão:
    else:
        # Retorna a media aritmetica das observações de X:
        return ma
    
# Nota sobre a função acima: observe que estou flexibilizando a restrição dos valores de X serem
# distintos, e que a frequência relativa de um valor qualquer pode ser zero (mas não todas elas).

# n: número de observações;
# X: observações ordenadas (estatísticas de ordem).
def mediana(n, X):
    # Se número de observações for menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Se n ímpar:
    if n%2:
        # Retorna a observação no centro da sequência:
        return X[int(n/2)]
    else:
        # Retorna a média aritmética entre as duas observações centrais:
        return ((X[int(n/2)-1] + X[int(n/2)])/2)

# n: número de observações;
# X: vetor de observações.
def moda(n, X):
    # Se número de observações for menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Inicia lista de pares de observações distintas e contagem de repetições:
    Y = [[X[0], 1]]
    # Número de obsevações distintas: 
    k = 1
    # Inicia lista de índices relativos as observações mais frequentes na lista de pares Y:
    Iv = [0]
    # Número de índices de observações mais frequentes:
    p = 1
    
    # Para todas as observações:
    for x in X[1:]:
        # Variável auxiliar para percorrer os pares de Y:
        j = 0
        # Para todas as observações distintas:
        for y in Y:
            # Se x é uma repetição:
            if x == y[0]:
                # Incrementa o número de repetíções:
                Y[j][1] += 1
                # Se a observação corrente repetiu mais vezes que uma das observações mais frequentes:
                if Y[j][1] > Y[Iv[0]][1]:
                    # Limpa a lista de índices de observações mais repetidas:
                    Iv.clear()
                    # Insere o índice da observação corrente:
                    Iv.append(j)
                    # Reinicia o número de índices:
                    p = 1
                # Senão, se a observação corrente repetiu o mesmo número de vezes:
                elif Y[j][1] == Y[Iv[0]][1]:
                    # Insere o índice da observação corrente:
                    Iv.append(j)
                    # Incrementa o número de índices:
                    p += 1
                # Sai do loop mais interno:
                break
            # Avança o auxiliar de índice:
            j += 1
        # Se passou por todos os elementos de Y:
        if j == k:
            # Insere observação distinta:
            Y.append([x, 1])
            # Incrementa o número de observações distintas:
            k += 1
            # Se a primeira observação mais frequente tiver frequência 1:
            if Y[Iv[0]][1] == 1:
                # Insere o índice da observação distinta inserida:
                Iv.append(j)
                # Incrementa o número de índices:
                p += 1
    
    # Retorna uma lista das observações mais frequentes:
    return [Y[Iv[i]][0] for i in range(0, p)]
