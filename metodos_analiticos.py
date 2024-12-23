# Importa o módulo metodos_descritivos como mdes:
import INMET.metodos_descritivos as mdes # type: ignore

# Y_t = \sum_{j=-q}^{s}{\alpha_j*X_{t+j}}
# \sum_{j=-q}^{s}{\alpha_j} = 1

# n: número de observações;
# X: vetor de observações;
# q: distância temporal à esquerda da (t+1)-ésima observação;
# s: distância temporal à direita da (t+1)-ésima observação;
# Alfa: vetor de pesos.
def plota_grafico_de_suavizacao_por_media_movel(n, X, q, s, Alfa):
    # Se alguma das distâncias temporais forem menores que zero:
    if q < 0 or s < 0:
        # Encerra programa:
        raise Exception("Erro. As distâncias temporais devem ser naturais não nulos.")

    # Se o tamanho do vetor alfa for diferente do tamanho da janela:
    if len(Alfa) != q+s:
        # Encerra programa:
        raise Exception(f"Erro: {len(Alfa)} != {q} + {s}.")

    # Se não há observações:
    if n < 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Se o número de observações for menor que o tamanho da janela:
    if n < q+s:
        # Encerra programa:
        raise Exception("Erro. O tamanho da janela deve ser menor que o número de observações.")

    # Inicia acumulador:
    acumulador = 0
    # Para todo alfa:
    for alfa in Alfa:
        # Acumula:
        acumulador += alfa
    # Se o acumulo de alfa for diferente de 1:
    if acumulador != 1:
        # Encerra programa:
        raise Exception("Erro. A soma dos elementos do vetor alfa deve resultar em 1.")

    # Cria série Y:
    Y = []

    # t+s <= n-1;
    #   t <= n-1-s.
    # t-q >= 0;
    #   t >= q.

    # Para todo t:
    for t in range(q, n-s):
        # Inicia acumulador:
        acumulador = 0
        # Para toda observação na janela:
        for j, x in enumerate(X[t-q:t+s]):
            # Acumula a suavização:
            acumulador += Alfa[j]*x
        # Salva a observação suavizada:
        Y.append(acumulador)
    
    mdes.plota_grafico_no_tempo([i for i in range(1, n-s-q+1)], Y, tipo="line", titulo=f"Suavização por Janela [{-q}, {s}]", rotulo_de_x="Tempo", rotulo_de_y="Valor Suavizado", grade=True, cor='blue')

# Para s = q:
# Y_t = \frac{1}{2q+1} \sum_{j=-q}^{q}{X_{t+j}}

# n: número de observações;
# X: vetor de observações;
# q: distância temporal à esquerda e à direita da (t+1)-ésima observação;
def suavizacao_por_media_movel_simplificada(n, X, q):
    # Se a distância temporal for menor que zero:
    if q < 0:
        # Encerra programa:
        raise Exception("Erro. A distância temporal deve ser um natural não nulo.")

    # Se não há observações:
    if n < 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")

    # Se o número de observações for menor que o tamanho da janela:
    if n < q+q:
        # Encerra programa:
        raise Exception("Erro. O tamanho da janela deve ser menor que o número de observações.")

    # Cria série Y:
    Y = []

    # Para todo t:
    for t in range(q, n-q):
        # Inicia acumulador:
        acumulador = 0
        # Para toda observação na janela:
        for x in X[t-q:t+q]:
            # Acumula a suavização:
            acumulador += x
        # Salva a observação suavizada:
        Y.append(acumulador*(1/(2*q+1)))
    
    mdes.plota_grafico_no_tempo([i for i in range(1, n-q-q+1)], Y, tipo="line", titulo=f"Suavização por Janela [{-q}, {q}]", rotulo_de_x="Tempo", rotulo_de_y="Valor Suavizado", grade=True, cor='blue')

