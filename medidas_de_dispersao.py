# Importa o módulo math:
import math
# Importa o módulo medidas_de_posicao como mpos
import INMET.medidas_de_posicao as mpos # type: ignore

# n: número de observações;
# X: vetor de observações.
def desvio_medio(n, X):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Calcula a média aritmética das observações:
    X_ma = mpos.media_aritmetica(n, X)
    # Inicia desvio médio:
    dm = 0

    # Para cada observação:
    for x in X:
        # Acumula o módulo da diferença entre a observação e a média da variável aleatória:
        dm += (x-X_ma) if x >= X_ma else (X_ma-x)

    # Retorna o desvio médio:
    return (dm/n)

# k: número de observações distintas;
# F: vetor de frequências relativas a cada observação distinta;
# X: vetor de observações distintas.
def desvio_medio_de_observacoes_distintas_com_frequencias_relativas_associadas(k, F, X):
    # Se número de observações distintas menor ou igual a zero:
    if k <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações distintas deve ser um natural não nulo.")

    # Calcula a média aritmética das observações:
    X_ma = mpos.media_aritmetica_de_observacoes_distintas_com_frequencias_relativas_associadas(k, F, X)
    # Inicia desvio médio:
    dm = 0
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
            dm += F[i]*((X[i]-X_ma) if X[i] >= X_ma else (X_ma-X[i]))
            # Incrementa a frequência total:
            f += F[i]
    
    # Se a frequência de observações total for diferente de 1:
    if f != 1:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Senão:
    else:
        # Retorna o desvio médio das observações de X:
        return dm
    
# Nota sobre a função acima: observe que estou flexibilizando a restrição dos valores de X serem
# distintos, e que a frequência relativa de um valor qualquer pode ser zero (mas não todas elas).

# n: número de observações;
# X: vetor de observações.
def variancia(n, X):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Calcula a média aritmética das observações:
    X_ma = mpos.media_aritmetica(n, X)
    # Inicia variância:
    v = 0

    # Para cada observação:
    for x in X:
        # Acumula o quadrado da diferença entre a observação e a média da variável aleatória:
        v += (x-X_ma)*(x-X_ma)

    # Retorna a variância:
    return (v/n)

# n: número de observações;
# X: vetor de observações.
def variancia_v2(n, X):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Inicia média aritmética das observações:
    X_ma = 0
    # Inicia variância:
    v = 0

    # Para cada observação:
    for x in X:
        # Acumula o quadrado:
        v += x*x
        # Acumula o valor:
        X_ma += x

    # Divide a variância pelo número de observações:
    v /= n
    # Divide a média aritmética pelo número de observações:
    X_ma /= n
    # Desconta o quadrado da média:
    v -= X_ma*X_ma

    # Retorna a variância:
    return (v/n)

# k: número de observações distintas;
# F: vetor de frequências relativas a cada observação distinta;
# X: vetor de observações distintas.
def variancia_de_observacoes_distintas_com_frequencias_relativas_associadas(k, F, X):
    # Se número de observações distintas menor ou igual a zero:
    if k <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações distintas deve ser um natural não nulo.")

    # Calcula a média aritmética das observações:
    X_ma = mpos.media_aritmetica_de_observacoes_distintas_com_frequencias_relativas_associadas(k, F, X)
    # Inicia variância:
    v = 0
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
            # Acumula a variância:
            v += F[i]*(X[i]-X_ma)*(X[i]-X_ma)
            # Incrementa a frequência total:
            f += F[i]
    
    # Se a frequência de observações total for diferente de 1:
    if f != 1:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Senão:
    else:
        # Retorna a variância das observações de X:
        return v
    
# Nota sobre a função acima: observe que estou flexibilizando a restrição dos valores de X serem
# distintos, e que a frequência relativa de um valor qualquer pode ser zero (mas não todas elas).

# k: número de observações distintas;
# F: vetor de frequências relativas a cada observação distinta;
# X: vetor de observações distintas.
def variancia_de_observacoes_distintas_com_frequencias_relativas_associadas_v2(k, F, X):
    # Se número de observações distintas menor ou igual a zero:
    if k <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações distintas deve ser um natural não nulo.")

    # Inicia média aritmética das observações:
    X_ma = 0
    # Inicia variância:
    v = 0
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
            # Acumula a média aritmética:
            X_ma += F[i]*X[i]
            # Acumula a variância:
            v += F[i]*X[i]*X[i]
            # Acumula a frequência total:
            f += F[i]
            
    # Se a frequência de observações total for diferente de 1:
    if f != 1:
        # Encerra o programa:
        raise Exception("Erro: a frequência não corresponde com o número de observações.")
    # Senão:
    else:
        # Retorna a variância das observações de X:
        return (v-(X_ma*X_ma))
    
# Nota sobre a função acima: observe que estou flexibilizando a restrição dos valores de X serem
# distintos, e que a frequência relativa de um valor qualquer pode ser zero (mas não todas elas).

# n: número de observações;
# X: vetor de observações.
def desvio_padrao(n, X):
    # Retorna a raíz quadrada da variância:
    return math.sqrt(variancia(n, X))
