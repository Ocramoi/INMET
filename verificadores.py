# Importa geradores_de_sequencias como gseq: 
import INMET.geradores_de_sequencias as gseq # type: ignore
# Importa math:
import math

"""
    Um número inteiro é primo se não é o número um ou seu oposto, e se somente é divisível
    por si mesmo, por seu oposto, por um, e pelo oposto de um, i.e., que tem como resultado
    um número também inteiro apenas na divisão de si por si mesmo, por seu oposto, por um e
    por oposto de um.
    
    Observação: o zero é divisível por todos inteiros (exceto (ou não),
                por si mesmo (python retorna erro de divisão por zero)).
"""
def eh_primo(nro):
    # Pega o módulo do número:
    nat_nro = abs(nro)
    # Se o número argumento é zero ou um ou o oposto de um:
    if nro == 0 or nat_nro == 1:
        # Então não é um número primo:
        return False
    # Calcula o limite multiplicativo (qualquer divisão
    #   por um número maior é menor que esse limite):
    lim = int(math.sqrt(nat_nro))
    # Calcula lista de primos até o limite:
    primos = gseq.crivo_de_eratostenes(lim)
    # Enquanto a lista de primos não estiver vazia:
    while not primos == []:
        # Se o módulo do número é divisível pelo menor primo da lista:
        if nat_nro%primos.pop(0) == 0:
            # então o número não é primo:
            return False
    # se o número não é divisível por nenhum dos primos até o limite:
    return True
