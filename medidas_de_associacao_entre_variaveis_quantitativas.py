# Importa o módulo math:
import math
# Importa o módulo medidas_de_posicao como mp:
import INMET.medidas_de_posicao as mpos # type: ignore
# Importa o módulo medidas_de_dispersao como md:
import INMET.medidas_de_dispersao as mdis # type: ignore

# n: número de observações;
# X1: um vetor de observações;
# X2: outro vetor de observações.
def covariancia(n, X1, X2):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Inicia a covariância entre X1 e X2:
    cov = 0
    # Calcula a média aritmética das observações da variável aleatória X1: 
    X1_ma = mpos.media_aritmetica(n, X1)
    # Calcula a média aritmética das observações da variável aleatória X2: 
    X2_ma = mpos.media_aritmetica(n, X2)
    # Para todas as observações:
    for t in range(0, n):
        # Atualiza a covariância:
        cov += ((X1[t] - X1_ma) * (X2[t] - X2_ma))
    # Retorna a covariância:
    return (cov/n)

# n: número de observações;
# X1: um vetor de observações;
# X2: outro vetor de observações.
def correlacao_v1(n, X1, X2):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Calcula a covariância entre X1 e X2:
    cov = covariancia(n, X1, X2)
    # Calcula o desvio padrão de X1:
    dp_X1 = mdis.desvio_padrao(n, X1)
    # Calcula o desvio padrão de X2:
    dp_X2 = mdis.desvio_padrao(n, X2)
    # Calcula o denominador do cálculo de correlação:
    denominador = dp_X1 * dp_X2 
    # Retorna a correlação entre X1 e X2:
    return (cov/denominador) if denominador != 0 else 1
# Observe que o desvio padrão é sempre >= 0.

# n: número de observações;
# X1: um vetor de observações;
# X2: outro vetor de observações.
def correlacao_v2(n, X1, X2):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Inicia a covariância entre X1 e X2:
    cov = 0
    # Inicia o desvio padrão de X1:
    dp_X1 = 0
    # Inicia o desvio padrão de X2:
    dp_X2 = 0
    # Calcula a média aritmética das observações da variável aleatória X1: 
    X1_ma = mpos.media_aritmetica(n, X1)
    # Calcula a média aritmética das observações da variável aleatória X2:
    X2_ma = mpos.media_aritmetica(n, X2)
    # Para todas as observações:
    for t in range(0, n):
        # Atualiza a covariância:
        cov += ((X1[t] - X1_ma) * (X2[t] - X2_ma))
        # Atualiza o desvio padrão de X1:
        dp_X1 += ((X1[t] - X1_ma) * (X1[t] - X1_ma))
        # Atualiza o desvio padrão de X2:
        dp_X2 += ((X2[t] - X2_ma) * (X2[t] - X2_ma))
    # Termina de calcular a covariância:
    cov /= n
    # Calcula o produto dos devios padrões parcialmente calculados:
    produto = dp_X1*dp_X2
    # Retorna a correlação entre X1 e X2:
    return (cov/math.sqrt(produto)) if produto != 0 else 1

# n: número de observações;
# X: vetor de observações;
# k: lag (defasagem).
def autocorrelacao_v1(n, X, k):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Se a defasagem solicitada for negativa ou maior que n-1:
    if k < 0 or k > n-1:
        # Encerra o programa:
        raise Exception("Erro. O passo de defasagem deve ser um natural pertencente ao intervalo [0, n-1].")
    # Inicia a autocovariância da variável aleatória x com defasagem k:
    autocov = 0
    # Inicia o desvio padrão das n-k primeiras observações da variável aleatória X:
    dp_X1 = 0
    # Inicia o desvio padrão das n-k últimas observações da variável aleatória X:
    dp_X2 = 0
    # Calcula a média aritmética das n-k primeiras observações da variável aleatória X:
    X1_ma = mpos.media_aritmetica(n-k, X)
    # Calcula a média aritmética das n-k últimas observações da variável aleatória X: 
    X2_ma = mpos.media_aritmetica(n-k, X[k:])
    # Para n-k observações:
    for t in range(0, n-k):
        # Atualiza a autocovariância:
        autocov += ((X[t] - X1_ma) * (X[t+k] - X2_ma))
        # Atualiza o desvio padrão das n-k primeiras observações da variável aleatória X:
        dp_X1 += ((X[t] - X1_ma) * (X[t] - X1_ma))
        # Atualiza o desvio padrão das n-k últimas observações da variável aleatória X:
        dp_X2 += ((X[t+k] - X2_ma) * (X[t+k] - X2_ma))
    # Termina de calcular a autocovariância:
    autocov /= n
    # Calcula o produto dos devios padrões parcialmente calculados:
    produto = dp_X1 * dp_X2
    # Retorna a autocorrelação de X com defasagem k:
    return (autocov/math.sqrt(produto)) if produto != 0 else 1

# n: número de observações;
# X: vetor de observações;
# k: lag (defasagem).
def autocorrelacao_v2(n, X, k):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Se a defasagem solicitada for negativa ou maior que n-1:
    if k < 0 or k > n-1:
        # Encerra o programa:
        raise Exception("Erro. O passo de defasagem deve ser um natural pertencente ao intervalo [0, n-1].")
    # Inicia a autocovariância da variável aleatória X com defasagem k:
    autocov = 0
    # Inicia uma simplificação para o produto do desvio padrão dos dois subconjuntos defasados de observações da variável aleatória X: 
    denominador = 0
    # Calcula a média aritmética das n observações (pois as médias das defasagens são aproximadamente iguais) da variável aleatória X:
    X_ma = mpos.media_aritmetica(n, X)
    # Para n-k observações:
    for t in range(0, n-k):
        # Atualiza a autocovariância:
        autocov += ((X[t] - X_ma) * (X[t+k] - X_ma))
        # Atualiza o denominador:
        denominador += ((X[t] - X_ma) * (X[t] - X_ma))
    # Retorna a autocorrelação de X com defasagem k:
    return (autocov/denominador) if denominador != 0 else 1
    # Comentário: a função autocorrelacao_v2 considera uma aproximação do denominador.
