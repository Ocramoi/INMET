# Importa math:
import math
# Função que retorna uma lista dos números primos
# naturais até o módulo de um dado número inteiro.
def crivo_de_eratostenes(nro):
    # pega o módulo do número:
    nat_nro = abs(nro)
    # Se o número argumento é zero ou um ou o oposto de um:
    if nro == 0 or nat_nro == 1:
        # retorna lista vazia:
        return []
    # inicia uma lista correspondente aos números naturais
    # entre [2, nat_nro] com sinais de que todos são primos
    nat_primos = [True for k in range(2, nat_nro+1, 1)]
    # calcula o limite multiplicativo (qualquer divisão
    #   por um número maior é menor que esse limite):
    lim = int(math.sqrt(nat_nro))
    # inicia lista de primos com lista vazia:
    primos = []
    # Itera pelo intervalo [2, lim]:
    for k in range(2, lim+1, 1):
        # Se o natural é primo:
        if nat_primos[k-2]:
            # adiciona na lista:
            primos.append(k)
             # inicia multiplo:
            m = k + k 
            # Enquanto o múltiplo não ultrapassar o módulo do número:
            while not m > nat_nro:
                # marca o múltiplo na lista como não-primo:
                nat_primos[m-2] = False
                # incrementa o múltiplo:
                m = m + k
    # Itera pelos demais naturais até o módulo do número:
    for k in range(lim+1, nro+1, 1):
        # Se o natural é primo:
        if nat_primos[k-2]:
            # adiciona na lista:
            primos.append(k)
    # limpa a lista de booleanos:
    nat_primos.clear()
    # retorna a lista de primos:
    return primos

# numero: número natural há ser descrito por seus divisores. 
def divisores(numero):
    # Inicializa a lista de divisores como lista vazia:
    div = []
    # Inicializa quantidade de divisores com zero:
    qtd = 0
    # Se o número for menor que zero:
    if numero < 0:
        # Encerra o programa:
        raise Exception("Erro. O número a ser descrito por seus divisores deve ser um número natural.")
    # Se o número é o zero:
    if not numero:
        # Retorna dupla de zero e lista vazia:
        return (qtd, div)
    # Inicia a lista de divisores com um:
    div.append(1)
    # Incrementa a quantidade de divisores:
    qtd += 1
    # Senão, se o número é o um:
    if numero == 1:
        # Retorna dupla 1 e lista com o um:
        return (qtd, div)
    # Calcula a lista de números primos até o número a ser descrito: 
    primos = crivo_de_eratostenes(numero)
    # Inicia quantidade de divisores corrente final:
    qtd_corr_f = 0
    # Para todos os primos
    for p in primos:
        # Inicia quantidade de divisores corrente inicial:
        qtd_corr_i = 0
        # Enquanto o número for divisível pelo primo corrente: 
        while not (numero%p):
            # Pega a quantidade de divisores corrente:
            qtd_corr_f = qtd
            # Para todos os últimos divisores salvos:
            for k in range(qtd_corr_i, qtd_corr_f):
                # Incrementa a quantidade de divisores:
                qtd += 1
                # Salva o divisor:
                div.append(p*div[k])
            # Atualiza o número:
            numero /= p
            # Atualiza a quantidade corrente inicial:
            qtd_corr_i = qtd_corr_f
        # Se calculou todos os fatores:
        if numero == 1:
            # Sai do loop:
            break
    # Ordena a lista:
    div.sort()
    # Retorna dupla de quantidade de divisores e a lista dos divisores ordenada:
    return (qtd, div)

# numero: número natural a ser decomposto;
def decomposicao_em_dupla_de_fatores_mais_proximos(numero):
    # Calcula os divisores de um número:
    n, X = divisores(numero)
    # Se o número de divisores for zero (o número decomposto é o zero):
    if not n:
        # Retorna lista vazia:
        return X
    # Se o número de divisores for ímpar:
    if n%2:
        # Retorna dupla do divisor central:
        return [X[int(n/2)], X[int(n/2)]]
        # Se o tipo de ajuste for à direita:
    # Senão:
    else:
        # Retorna dupla central:
        return [X[int(n/2)-1], X[int(n/2)]]


# lista: lista de elementos.
def imprime_lista(lista):
    # Abre a lista:
    print("[", end='')
    # Para todos os elementos da lista (exceto o último):
    for e in lista[:-1]:
        # Imprime elemento:
        print(f"{e}, ", end='')
    # Imprime o último elemento e fecha a lista:
    print(f"{lista[-1]}]")

# numero = int(input("Digite o número a ser descrito por seus divisores: "))
# qtd, div = divisores(numero)
# imprime_lista(div)

# dupla_de_fatores_mais_proximos = decomposicao_em_dupla_de_fatores_mais_proximos(numero)
# imprime_lista(dupla_de_fatores_mais_proximos)
