# Importa medidas_de_associacao_entre_variaveis_quantitativas como ma:
import INMET.medidas_de_associacao_entre_variaveis_quantitativas as mava # type: ignore
# Importa pyplot como plt:
import matplotlib.pyplot as plt
# Importa pandas como pd:
import pandas as pd
# Importa numpy como np:
import numpy as np
# Importa geradores_de_sequencias como gseq:
import INMET.geradores_de_sequencias as gseq # type: ignore
# Importa verificadores como ver:
import INMET.verificadores as ver # type: ignore
from typing import Union

# X: lista ou array de dados no eixo x;
# Y: lista ou array de dados no eixo y;
# tipo: tipo de gráfico (aceita 'line' ou 'scatter' ou 'bar') (está sendo iniciado como 'line' por padrão).
# titulo: título do gráfico (está sendo iniciada como None por padrão).
# rotulo_de_x: rótulo do eixo x (está sendo iniciado como None por padrão).
# rotulo_de_y: rótulo do eixo y (está sendo iniciado como None por padrão).
# grade: indica se o gráfico deve ter grid (está sendo iniciado como True por padrão).
# legenda: legenda do gráfico (está sendo iniciada como None por padrão).
# cor: cor da linha (ou pontos) (está sendo iniciada como 'blue' por padrão).
def plota_grafico_no_tempo(
        X,
        Y,
        tipo: str = 'line',
        titulo: Union[str, None] = None,
        rotulo_de_x: Union[str, None] = None,
        rotulo_de_y: Union[str, None] = None,
        grade: bool = True,
        legenda: Union[str, None] = None,
        cor: str = 'blue'
):
    # Cria o gráfico conforme o tipo solicitado:
    if tipo == 'line':
        plt.plot(X, Y, label=legenda, color=cor)
    elif tipo == 'scatter':
        plt.scatter(X, Y, label=legenda, color=cor)
    elif tipo == 'bar':
        plt.bar(X, Y, label=legenda, color=cor)
    else:
        raise Exception(f"Tipo de gráfico '{tipo}' não suportado. Será usado o tipo 'line'.")

    # Adiciona título e rótulos aos eixos, se fornecidos:
    if titulo:
        plt.title(titulo)
    if rotulo_de_x:
        plt.xlabel(rotulo_de_x)
    if rotulo_de_y:
        plt.ylabel(rotulo_de_y)

    # Exibe a legenda, se fornecida:
    if legenda:
        plt.legend()

    # Secciona o gráfico por linhas e colunas:
    if grade:
        plt.grid(True)


# n: número de observações;
# X: vetor de observações.
def plota_correlograma(n: int, X: np.ndarray, d: Union[int, None]):
    if d:
        assert isinstance(d, int)
        _plota_correlograma(n, X, d)
        return
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Cria eixo x referente as defasagens:
    defasagem = []
    # Cria eixo y referente as autocorrelações:
    autocor = []
    # Para todas as defasagens possíveis:
    for k in range(0, n):
        print(k, '/', n - 1)
        # Salva a defasagem:
        defasagem.append(k)
        # Salva a autocorrelação relacionada a defasagem:
        autocor.append(mava.autocorrelacao_v1(n, X, k))
    # Plota gráfico de barras respectivo ao correlograma:
    plota_grafico_no_tempo(np.array(defasagem), np.array(autocor), tipo='bar', titulo="Correlograma", rotulo_de_x="Defasagem", rotulo_de_y="Correlação", grade=False, cor='blue')

# n: número de observações;
# X: vetor de observações;
# d: defasagem máxima.
def _plota_correlograma(n: int, X: np.ndarray, d: int):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Se defasagem máxima maior que o número de observações: 
    if d >= n:
        # Imprime mensagem de erro:
        raise Exception("Erro. A defasagem máxima deve ser menor que o número de observações.")
    # Cria eixo x referente as defasagens:
    defasagem = []
    # Cria eixo y referente as autocorrelações:
    autocor = []
    # Para todas as defasagens possíveis:
    for k in range(d):
        # Salva a defasagem:
        defasagem.append(k)
        # Salva a autocorrelação relacionada a defasagem:
        autocor.append(mava.autocorrelacao_v1(n, X, k))
    # Plota gráfico de barras respectivo ao correlograma:
    plota_grafico_no_tempo(X=np.array(defasagem), Y=np.array(autocor, dtype=np.float64), tipo='bar', titulo="Correlograma", rotulo_de_x="Defasagem", rotulo_de_y="Correlação", grade=False, cor='blue')

# n: número de observações;
# X: vetor de observações;
# k: distância temporal.
def plota_grafico_de_defasagens(n: int, X: np.ndarray, k: int):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Se a defasagem solicitada for negativa ou maior que n-1:
    if k < 0 or k > n - 1:
        # Encerra o programa:
        raise Exception(f"Erro. O passo de defasagem deve ser um natural pertencente ao intervalo [0, {n}-1].")
    # Plota gráfico de pontos para a defasagem:
    # plota_grafico_no_tempo(X[:n-k], X[k:], tipo='scatter', titulo=f"Gráfico de Defasagens de Passo {k}", rotulo_de_x="$X_t$", rotulo_de_y=f"$X_{{t-{k}}}$", grade=True, cor='blue')
    # Cria o gráfico:
    plt.scatter(X[:n-k], X[k:], color='blue', s=1, alpha=0.5)
    # Adiciona linha tracejada na diagonal:
    plt.plot([min(X[:n-k]), max(X[:n-k])], [min(X[k:]), max(X[k:])], linestyle='--', color='red')
    # Adiciona título:
    plt.title(f"Gráfico de Defasagem {k}")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("$X_t$")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"$X_{{t-{k}}}$")

# n: número de observações;
# X: vetor de observações;
# k: distância temporal limite.
def plota_grafico_de_multiplos_graficos_de_defasagens(n: int, X: np.ndarray, k: int):
    # Se número de observações menor ou igual a zero:
    if n <= 0:
        # Encerra o programa:
        raise Exception("Erro. O número de observações deve ser um natural não nulo.")
    # Se a defasagem limite solicitada for negativa ou maior que n-1:
    if k < 0 or k > n-1:
        # Encerra o programa:
        raise Exception(f"Erro. O passo de defasagem limite deve ser um natural pertencente ao intervalo [0, {n}-1].")
    # Se k for zero ou um:
    if not k or k == 1:
        # Plota gráfico simples de defasagem:
        plota_grafico_de_defasagens(n, X, k)
        return None
    # Senão, se k for dois:
    elif k == 2:
        # Cria vetor de gráficos:
        fig, axes = plt.subplots(1, 2, figsize=(15, 10))
        # Para todas as defasagens:
        for i in range(1, 3):
           # Cria o gráfico:
            axes[i-1].scatter(X[:n-i], X[i:], color='blue', s=1, alpha=0.5)
            # Adiciona linha tracejada na diagonal:
            axes[i-1].plot([min(X[:n-i]), max(X[:n-i])], [min(X[i:]), max(X[i:])], linestyle='--', color='red')
            # Adiciona título:
            axes[i-1].set_title(f"Gráfico de Defasagem {i}")
            # Adiciona rótulo ao eixo x:
            axes[i-1].set_xlabel("$X_t$")
            # Adiciona rótulo ao eixo y:
            axes[i-1].set_ylabel(f"$X_{{t-{i}}}$")
    # Senão:
    else:
        # Inicia indicador de tamanho de passo:
        z = 1
        # Se k for ímpar:
        if k%2:
            # Se k é primo:
            if ver.eh_primo(k):
                # Pega os dois fatores dos quais o maior deles é o menor possível para ser maior
                # das possibilidades de pares de fatores que se multiplicados descrevem k+1:
                f = gseq.decomposicao_em_dupla_de_fatores_mais_proximos(k+1)
                # print(f"({f[0]}, {f[1]})")
                # Cria matriz de gráficos:
                fig, axes = plt.subplots(f[0], f[1], figsize=(15, 10))
                # Para todas as linhas (exceto a última):
                for i in range(0, f[0]-1):
                    # Para todas as colunas:
                    for j in range(0, f[1]):
                        # Cria o gráfico:
                        axes[i, j].scatter(X[:n-z], X[z:], color='blue', s=1, alpha=0.5)
                        # Adiciona linha tracejada na diagonal:
                        axes[i, j].plot([min(X[:n-z]), max(X[:n-z])], [min(X[z:]), max(X[z:])], linestyle='--', color='red')
                        # Adiciona título:
                        axes[i, j].set_title(f"Gráfico de Defasagem {z}")
                        # Adiciona rótulo ao eixo x:
                        axes[i, j].set_xlabel("$X_t$")
                        # Adiciona rótulo ao eixo y:
                        axes[i, j].set_ylabel(f"$X_{{t-{z}}}$")
                        # Aumenta o passo:
                        z += 1
                # Para todas as colunas (exceto a última) da última linha:
                for j in range(0, f[1]-1):
                    # Cria o gráfico:
                    axes[f[0]-1, j].scatter(X[:n-z], X[z:], color='blue', s=1, alpha=0.5)
                    # Adiciona linha tracejada na diagonal:
                    axes[f[0]-1, j].plot([min(X[:n-z]), max(X[:n-z])], [min(X[z:]), max(X[z:])], linestyle='--', color='red')
                    # Adiciona título:
                    axes[f[0]-1, j].set_title(f"Gráfico de Defasagem {z}")
                    # Adiciona rótulo ao eixo x:
                    axes[f[0]-1, j].set_xlabel("$X_t$")
                    # Adiciona rótulo ao eixo y:
                    axes[f[0]-1, j].set_ylabel(f"$X_{{t-{z}}}$")
                    # Aumenta o passo:
                    z += 1
                # Desativa a exibição da última célula de gráfico:
                axes[f[0]-1, f[1]-1].axis('off')
            # Senão:
            else:
                # Pega os dois fatores dos quais o maior deles é o menor possível para ser maior
                # das possibilidades de pares de fatores que se multiplicados descrevem k:
                f = gseq.decomposicao_em_dupla_de_fatores_mais_proximos(k)
                # print(f"({f[0]}, {f[1]})")
                # Cria matriz de gráficos:
                fig, axes = plt.subplots(f[0], f[1], figsize=(15, 10))
                # Para todas as linhas:
                for i in range(0, f[0]):
                    # Para todas as colunas:
                    for j in range(0, f[1]):
                        # Cria o gráfico:
                        axes[i, j].scatter(X[:n-z], X[z:], color='blue', s=1, alpha=0.5)
                        # Adiciona linha tracejada na diagonal:
                        axes[i, j].plot([min(X[:n-z]), max(X[:n-z])], [min(X[z:]), max(X[z:])], linestyle='--', color='red')
                        # Adiciona título:
                        axes[i, j].set_title(f"Gráfico de Defasagem {z}")
                        # Adiciona rótulo ao eixo x:
                        axes[i, j].set_xlabel("$X_t$")
                        # Adiciona rótulo ao eixo y:
                        axes[i, j].set_ylabel(f"$X_{{t-{z}}}$")
                        # Aumenta o passo:
                        z += 1
        # Senão, se k par:
        else:
            # Pega os dois fatores dos quais o maior deles é o menor possível para ser maior
            # das possibilidades de pares de fatores que se multiplicados descrevem k:
            f = gseq.decomposicao_em_dupla_de_fatores_mais_proximos(k)
            # print(f"({f[0]}, {f[1]})")
            # Cria matriz de gráficos:
            fig, axes = plt.subplots(f[0], f[1], figsize=(15, 10))
            # Para todas as linhas:
            for i in range(0, f[0]):
                # Para todas as colunas:
                for j in range(0, f[1]):
                    # Cria o gráfico:
                    axes[i, j].scatter(X[:n-z], X[z:], color='blue', s=1, alpha=0.5)
                    # Adiciona linha tracejada na diagonal:
                    axes[i, j].plot([min(X[:n-z]), max(X[:n-z])], [min(X[z:]), max(X[z:])], linestyle='--', color='red')
                    # Adiciona título:
                    axes[i, j].set_title(f"Gráfico de Defasagem {z}")
                    # Adiciona rótulo ao eixo x:
                    axes[i, j].set_xlabel("$X_t$")
                    # Adiciona rótulo ao eixo y:
                    axes[i, j].set_ylabel(f"$X_{{t-{z}}}$")
                    # Aumenta o passo:
                    z += 1

    # Ajusta layout para evitar sobreposição de labels:
    plt.tight_layout()
    return fig


# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# m: mês a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_mes(
        df: pd.DataFrame,
        atr_temporal: str,
        atr_imagem: str,
        m: int
):
    # Se m não for um mês válido:
    if m < 1 or m > 12:
      # Encerra o programa:
      raise Exception("Mês inválido. O indicador deve pertencer ao intervalo de naturais [1, 12].")
    # Filtra as tuplas onde a data pertence ao mês m:
    df_filtrado = df[(df[atr_temporal].dt.month == m)].copy()
    # Cria uma coluna com o formato dia:
    df_filtrado.loc[:, 'Dia'] = df_filtrado[atr_temporal].dt.strftime('%d')
    # Agrupa as tuplas filtradas pelos dias e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Dia')[atr_imagem].mean()
    # Ordena as médias pelos dias em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (dia, média):
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_mensal(df, atr_temporal, atr_imagem):
    # Converte o atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Lista de nomes dos meses:
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    # Usa paleta 'tab20' para gerar 12 cores diferentes:
    cor = plt.cm.tab20(np.linspace(0, 1, 12))
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um mês:
    mes = []
    # Para todos os meses de um ano:
    for m in range(1, 13):
        # Obtém a lista de tuplas (dia, média):
        mes.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_mes(df_filtrado, atr_temporal, atr_imagem, m))
        # Cria o gráfico (o eixo X será os índices dos dias do mês e o eixo Y será a média (M[1])):
        # plt.plot([M[0] for M in mes[m-1]], [M[1] for M in mes[m-1]], color=cor[m-1], label=f'{meses[m-1]}')
        plt.plot(list(range(len(mes[m-1]))), [M[1] for M in mes[m-1]], color=cor[m-1], label=f'{meses[m-1]}')
    # Adiciona título:
    plt.title("Sazonalidade Mensal")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# b: bimestre a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_bimestre(
        df: pd.DataFrame,
        atr_temporal: str,
        atr_imagem: str,
        b: int
):
    # Se indicador de bimestre inválido:
    if b < 1 or b > 6:
      # Encerra o programa:
      raise Exception("Bimestre inválido. O indicador deve pertencer ao intervalo de naturais [1, 6].")
    # Filtra as tuplas onde a data pertence ao b-ésimo bimestre de algum ano:
    df_filtrado = df[(df[atr_temporal].dt.month >= 2*(b-1)+1) & (df[atr_temporal].dt.month <= 2*b)].copy()
    # Cria uma coluna com o formato mês-dia:
    df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
    # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()
    # Ordena as médias pela data (dia e mês) em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é dia e mês:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
def plota_grafico_de_sazonalidade_bimestral(
        df: pd.DataFrame,
        atr_temporal: str,
        atr_imagem: str
):
    # Converte o atributo atr_imagem para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um bimestre:
    bimestre = []
    # Para todos os bimestres de um ano:
    for b in range(1, 7):
      # Obtém a lista de tuplas (data, média):
      bimestre.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_bimestre(df_filtrado, atr_temporal, atr_imagem, b))
      # Cria o gráfico (o eixo X será referente a dia-mês (B[0]) e o eixo Y será a média (B[1])):
      plt.plot([i for i in range(1, len(bimestre[b-1])+1)], [B[1] for B in bimestre[b-1]], color=plt.cm.get_cmap('hsv', 7)(b - 1), label=f'Bimestre {b}')
    # Adiciona título:
    plt.title("Sazonalidade Bimestral")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# t: trimestre a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_trimestre(
        df: pd.DataFrame,
        atr_temporal: str,
        atr_imagem: str,
        t: int
):
    # Se indicador de trimestre inválido:
    if t < 1 or t > 4:
      # Encerra o programa:
      raise Exception("Trimestre inválido. O indicador deve pertencer ao intervalo de naturais [1, 4].")
    # Filtra as tuplas onde a data pertence ao t-ésimo trimestre de algum ano:
    df_filtrado = df[(df[atr_temporal].dt.month >= 3*(t-1)+1) & (df[atr_temporal].dt.month <= 3*t)].copy()
    # Cria uma coluna com o formato mês-dia:
    df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
    # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()
    # Ordena as médias pela data (dia e mês) em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é dia e mês:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_trimestral(df, atr_temporal, atr_imagem):
    # Converte o atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um trimestre:
    trimestre = []
    # Define uma cor para cada linha formada por cada trimestre:
        # Usa paleta 'tab10' para gerar 4 cores diferentes:
    cor = plt.cm.tab10(np.linspace(0, 1, 4))
    # Para todos os trimestres de um ano:
    for t in range(1, 5):
      # Obtém a lista de tuplas (data, média):
      trimestre.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_trimestre(df_filtrado, atr_temporal, atr_imagem, t))
      # Cria o gráfico (o eixo X será referente a dia-mês (T[0]) e o eixo Y será a média (T[1])):
      plt.plot([i for i in range(1, len(trimestre[t-1])+1)], [T[1] for T in trimestre[t-1]], color=cor[t-1], label=f'Trimestre {t}')
    # Adiciona título:
    plt.title("Sazonalidade Trimestral")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# q: quadrimestre a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_quadrimestre(df, atr_temporal, atr_imagem, q):
    # Se indicador de quadrimestre inválido:
    if q < 1 or q > 3:
      # Encerra o programa:
      raise Exception("Quadrimestre inválido. O indicador deve pertencer ao intervalo de naturais [1, 3].")
    # Filtra as tuplas onde a data pertence ao q-ésimo quadrimestre de algum ano:
    df_filtrado = df[(df[atr_temporal].dt.month >= 4*(q-1)+1) & (df[atr_temporal].dt.month <= 4*q)].copy()
    # Cria uma coluna com o formato mês-dia:
    df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
    # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()
    # Ordena as médias pela data (dia e mês) em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é dia e mês:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_quadrimestral(df, atr_temporal, atr_imagem):
    # Converte o atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um quadrimestre:
    quadrimestre = []
    # Define uma cor para cada linha formada por cada quadrimestre:
        # Usa paleta 'tab10' para gerar 3 cores diferentes:
    cor = plt.cm.tab10(np.linspace(0, 1, 3))
    # Para todos os quadrimestres de um ano:
    for q in range(1, 4):
      # Obtém a lista de tuplas (data, média):
      quadrimestre.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_quadrimestre(df_filtrado, atr_temporal, atr_imagem, q))
      # Cria o gráfico (o eixo X será referente a dia-mês (Q[0]) e o eixo Y será a média (Q[1])):
      plt.plot([i for i in range(1, len(quadrimestre[q-1])+1)], [Q[1] for Q in quadrimestre[q-1]], color=cor[q-1], label=f'Quadrimestre {q}')
    # Adiciona título:
    plt.title("Sazonalidade Quadrimestral")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# t: semestre a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_semestre(df, atr_temporal, atr_imagem, t):
    # Se indicador de semestre inválido:
    if(t < 1 or t > 2):
      # Encerra o programa:
      raise Exception("Semestre inválido. O indicador deve pertencer ao conjunto de naturais {1, 2}.")
    # Filtra as tuplas onde a data pertence ao t-ésimo semetre de algum ano:
    df_filtrado = df[(df[atr_temporal].dt.month >= 6*(t-1)+1) & (df[atr_temporal].dt.month <= 6*t)].copy()
    # Cria uma coluna com o formato mês-dia:
    df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
    # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()
    # Ordena as médias pela data (dia e mês) em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é dia e mês:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_semestral(df, atr_temporal, atr_imagem):
    # Converte o atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um semestre:
    semestre = []
    # Define uma cor para cada linha formada por cada semestre:
    cor = ['black', 'blue']
    # Para todos os semestres de um ano:
    for t in range(1, 3):
      # Obtém a lista de tuplas (data, média):
      semestre.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_semestre(df_filtrado, atr_temporal, atr_imagem, t))
      # Cria o gráfico (o eixo X será o dia-mês (m[0]) e o eixo Y será a média (m[1])):
      plt.plot([i for i in range(1, len(semestre[t-1])+1)], [m[1] for m in semestre[t-1]], color=cor[t-1], label=f'Semestre {t}')
    # Adiciona título:
    plt.title("Sazonalidade Semestral")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# n: número de cores.
def gerar_lista_de_cores(n):
    # Gera n cores uniformemente distribuídas no espaço de matiz (entre 0 e 1):
    hues = np.linspace(0, 1, n, endpoint=False)
    # Mapeia esses valores para cores no espaço HSV (matiz, saturação, valor):
    cores = plt.cm.hsv(hues)
    return cores

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# a: ano a ser analisado.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_ano(df, atr_temporal, atr_imagem, a):
    # Filtra as tuplas onde a data pertence ao ano t:
    df_filtrado = df[(df[atr_temporal].dt.year == a)].copy()
    # Agrupa as tuplas filtradas pelos dias e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby(atr_temporal)[atr_imagem].mean()
    # Ordena as médias do ano em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é ano:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_anual(df, atr_temporal, atr_imagem):
    # Converte atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Pega os anos do dataframe:
    anos = df[atr_temporal].dt.year.unique()
    # Define uma cor para cada linha formada por cada ano:
    cor = gerar_lista_de_cores(len(anos))
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante um ano:
    ano = []
    # Para todos os anos do dataframe:
    for i, t in enumerate(anos):
        # Obtém a lista de tuplas (data, média) para o ano t:
        ano.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_ano(df_filtrado, atr_temporal, atr_imagem, t))
        # Cria o gráfico (o eixo X será os índices dos dias do ano (0, 1, 2, ...) e o eixo Y será a média (m[1])):
        plt.plot(list(range(len(ano[i]))), [m[1] for m in ano[i]], color=cor[i], label=f'{t}')
    # Adiciona título:
    plt.title("Sazonalidade Anual")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# p: tipo de subperíodo de um ano a ser analisado;
# t: índice do subperíodo;
# a: ano a ser analisado (se p == 12 & t == 1).
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_periodo(df, atr_temporal, atr_imagem, p, t, a):
    
    # Se tipo de subperíodo inválido:
    if p < 1 or p > 12:
      # Encerra o programa:
      raise Exception("Tipo de subperíodo inválido. O tipo deve pertencer ao conjunto {1, 2, 3, 4, 6, 12}.")

    # Se indicador de subperíodo inválido:
    if t < 1 or t > int(12/p):
      # Se período anual:
      if p == 12:
        # Imprime respectiva mensagem de erro:
        raise Exception("Ano inválido. O indicador de subperíodo deve ser 1.")
      # Senão:
      else:
        # Imprime respectiva mensagem de erro:
        periodo = ''
        if p == 1:
          periodo = 'Mês'
        elif p == 2:
          periodo = 'Bimestre'
        elif p == 3:
          periodo = 'Trimestre'
        elif p == 4:
          periodo = 'Quadrimestre'
        elif p == 6:
          periodo = 'Semestre'
        elif p == 12:
          periodo = 'Ano'
        # Encerra o programa:
        raise Exception(f"{periodo} inválido. O indicador deve pertencer ao intervalo de naturais [1, {12/p}].")

    # Se sazonalidade mensal:
    if p == 1:
      # Filtra as tuplas onde a data pertence ao mês t:
      df_filtrado = df[(df[atr_temporal].dt.month == t)].copy()
      # Cria uma coluna com o formato dia:
      df_filtrado.loc[:, 'Dia'] = df_filtrado[atr_temporal].dt.strftime('%d')
      # Agrupa as tuplas filtradas pelos dias e calcula a média do atributo para cada grupo:
      media_por_dia = df_filtrado.groupby('Dia')[atr_imagem].mean()
    # Se sazonalidade anual:
    elif p == 12:
      # Filtra as tuplas onde a data pertence ao ano t:
      df_filtrado = df[(df[atr_temporal].dt.year == a)].copy()
      # Agrupa as tuplas filtradas pelos dias e calcula a média do atributo para cada grupo:
      media_por_dia = df_filtrado.groupby(atr_temporal)[atr_imagem].mean()
    # Senão, se sazonalidade bimestral ou trimestral ou quadrimestral ou semestral:
    else:
      # Filtra as tuplas onde a data pertence ao t-ésimo período de algum ano:
      df_filtrado = df[(df[atr_temporal].dt.month >= p*(t-1)+1) & (df[atr_temporal].dt.month <= p*t)].copy()
      # Cria uma coluna com o formato mês-dia:
      df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
      # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
      media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()

    # Ordena as médias pela data em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média):
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado.
def plota_grafico_de_sazonalidade_geral(df, atr_temporal, atr_imagem):

    # Converte o atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]

    # Tipos de períodos:
    P = [1, 2, 3, 4, 6, 12]
    # Nomes dos subperíodos:
    nomes_1 = ['Mês', 'Bimestre', 'Trimestre', 'Quadrimestre', 'Semestre']
    nomes_2 = ['Mensal', 'Bimestral', 'Trimestral', 'Quadrimestral', 'Semestral']
    # Cria matriz de gráficos 2x3:
    fig, axes = plt.subplots(2, 3, figsize=(15, 10), clear=True)
    # Cria lista para sequência (de passo temporal 1 dia) de médias de um atributo durante um período:
    periodos = []

    # Gera cores para os meses:
    cores_dos_meses = plt.cm.tab20(np.linspace(0, 1, 12))

    # Para todos os gráficos na 1a linha: 
    for c in range(0, 3):
        # Para todas as curvas do tipo de período:
        for t in range(1, int(12/P[c])+1):
            # Obtém a lista de tuplas (dia, média):
            periodos.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_periodo(df_filtrado, atr_temporal, atr_imagem, P[c], t, 0))
            # Cria o gráfico (o eixo X será os índices dos dias e o eixo Y será a média (m[1])):
            # axes[0, c].plot([d[0] for d in periodos[t-1]], [m[1] for m in periodos[t-1]], color=cores_dos_meses[t-1], label=f'{nomes_1[c]} {t}')
            axes[0, c].plot(list(range(len(periodos[t-1]))), [m[1] for m in periodos[t-1]], color=cores_dos_meses[t-1], label=f'{nomes_1[c]} {t}')
        # Adiciona título:
        axes[0, c].set_title(f"Sazonalidade {nomes_2[c]}")
        # Adiciona rótulo ao eixo x:
        axes[0, c].set_xlabel("Índice de Ordem Temporal Relativa")
        # Adiciona rótulo ao eixo y:
        axes[0, c].set_ylabel(f"Média de {atr_imagem}")
        # Adiciona a legenda:
        axes[0, c].legend()
        # Limpa a lista de períodos:
        periodos.clear()

    # Para todos (exceto o último) gráfico na 2a linha: 
    for c in range(0, 2):
      # Para todas as curvas do tipo de período:
        for t in range(1, int(12/P[3+c])+1):
            # Obtém a lista de tuplas (dia, média):
            periodos.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_periodo(df_filtrado, atr_temporal, atr_imagem, P[3+c], t, 0))
            # Cria o gráfico (o eixo X será os índices dos dias e o eixo Y será a média (m[1])):
            # axes[1, c].plot([d[0] for d in periodos[t-1]], [m[1] for m in periodos[t-1]], color=cores_dos_meses[t-1], label=f'{nomes_1[3+c]} {t}')
            axes[1, c].plot(list(range(len(periodos[t-1]))), [m[1] for m in periodos[t-1]], color=cores_dos_meses[t-1], label=f'{nomes_1[3+c]} {t}')
        # Adiciona título:
        axes[1, c].set_title(f"Sazonalidade {nomes_2[3+c]}")
        # Adiciona rótulo ao eixo x:
        axes[1, c].set_xlabel("Índice de Ordem Temporal Relativa")
        # Adiciona rótulo ao eixo y:
        axes[1, c].set_ylabel(f"Média de {atr_imagem}")
        # Adiciona a legenda:
        axes[1, c].legend()
        # Limpa a lista de períodos:
        periodos.clear()

    # Pega os anos do dataframe:
    anos = df[atr_temporal].dt.year.unique()
    # Gera cores para os anos:
    cores_dos_anos = plt.cm.tab20(np.linspace(0, 1, len(anos)))

    # Para todos os anos do dataframe:
    for i, ano in enumerate(anos):
        # Obtém a lista de tuplas (data, média) para o ano:
        periodos.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_um_periodo(df_filtrado, atr_temporal, atr_imagem, 12, 1, ano))
        # Cria o gráfico (o eixo X será os índices dos dias do ano (0, 1, 2, ...) e o eixo Y será a média (m[1])):
        axes[1, 2].plot(list(range(len(periodos[i]))), [m[1] for m in periodos[i]], color=cores_dos_anos[i], label=f'Ano {i}')
    # Adiciona título:
    axes[1, 2].set_title("Sazonalidade Anual")
    # Adiciona rótulo ao eixo x:
    axes[1, 2].set_xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    axes[1, 2].set_ylabel(f"Média de {atr_imagem}")

    # Ajusta layout para evitar sobreposição de labels:
    plt.tight_layout()
    return fig


# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# e: estação a ser analisada.
def lista_medias_de_um_atributo_agrupado_pelos_dias_de_uma_estacao_do_ano(df, atr_temporal, atr_imagem, e):
    # Se indicador de estação inválido:
    if e < 1 or e > 4:
        # Encerra o programa:
        raise Exception("Estação inválida. O indicador deve pertencer ao intervalo de naturais [1, 4].")
    # Filtra as tuplas onde a data pertence a e-ésima estação de algum ano:
    # é 12 menos (o seguinte menos o (passo menos um), módulo 12): ((4-1)*e - (4-1))%12.
    df_filtrado = df[((df[atr_temporal].dt.month == 12-((4-1)*e-(4-1))%12) & (df[atr_temporal].dt.day >= 21)) | 
                    (df[atr_temporal].dt.month == 12-((4-1)*e-(4-2))%12) |
                    (df[atr_temporal].dt.month == 12-((4-1)*e-(4-3))%12) |
                    ((df[atr_temporal].dt.month == (4-1)*e) & (df[atr_temporal].dt.day <= 20))].copy()
    # Cria uma coluna com o formato mês-dia:
    df_filtrado.loc[:, 'Mes_Dia'] = df_filtrado[atr_temporal].dt.strftime('%m-%d')
    # Agrupa as tuplas filtradas pelos dias e meses (ignorando o ano) e calcula a média do atributo para cada grupo:
    media_por_dia = df_filtrado.groupby('Mes_Dia')[atr_imagem].mean()
    # Ordena as médias pela data (dia e mês) em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (data, média), onde data é dia e mês:
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado,
def plota_grafico_de_sazonalidade_de_estacoes_do_ano(df, atr_temporal, atr_imagem):
    # Converteo atributo atr_temporal para o tipo datetime, caso ainda não esteja nesse formato:
    df[atr_temporal] = pd.to_datetime(df[atr_temporal])
    # Seleciona apenas o atributo temporal e o atributo imagem:
    df_filtrado = df[[atr_temporal, atr_imagem]]
    # Cria lista para sequência (de passo temporal 1) de médias de um atributo durante uma estação:
    estacoes = []
    # Nomes das estações:
    nomes = ['Verão', 'Outono', 'Inverno', 'Primavera']
    # Define uma cor para cada linha formada por cada estação:
        # Usa paleta 'tab10' para gerar 4 cores diferentes:
    cores = plt.cm.tab10(np.linspace(0, 1, 4))
    # Para todos as estações de um ano:
    for e in range(1, 5):
      # Obtém a lista de tuplas (data, média):
      estacoes.append(lista_medias_de_um_atributo_agrupado_pelos_dias_de_uma_estacao_do_ano(df_filtrado, atr_temporal, atr_imagem, e))
      # Cria o gráfico (o eixo X será referente a dia-mês (E[0]) e o eixo Y será a média (E[1])):
      plt.plot([i for i in range(1, len(estacoes[e-1])+1)], [Q[1] for Q in estacoes[e-1]], color=cores[e-1], label=f'{nomes[e-1]}')
    # Adiciona título:
    plt.title("Sazonalidade das Estações de Ano")
    # Adiciona rótulo ao eixo x:
    plt.xlabel("Índice de Ordem Temporal Relativa")
    # Adiciona rótulo ao eixo y:
    plt.ylabel(f"Média de {atr_imagem}")
    # Adiciona a legenda:
    plt.legend()

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado,
def lista_medias_de_um_atributo_agrupado_pelos_dias(df, atr_temporal, atr_imagem):
    # Agrupa as tuplas pelos dias e calcula a média do atributo para cada grupo:
    media_por_dia = df.groupby(atr_temporal)[atr_imagem].mean()
    # Ordena as médias pelos dias em ordem crescente:
    media_por_dia_ordenada = media_por_dia.sort_index()
    # Retorna lista de tuplas (dia, média):
    return list(media_por_dia_ordenada.items())

# df: dataframe a ser analisado;
# atr_temporal: atributo do tipo date;
# atr_imagem: atributo a ser analisado;
# tt: título fdo gráfico;
# ry: rótulo de y;
def plota_grafico_no_tempo_sumarizado_por_dia(df, atr_temporal, atr_imagem, tt, ry):
  # Lista as médias dos grupos de valores do atributo imagem agrupados por cada data do período:
  periodo = lista_medias_de_um_atributo_agrupado_pelos_dias(df, atr_temporal, atr_imagem)
  plota_grafico_no_tempo([P[0] for P in periodo], [P[1] for P in periodo], titulo=tt, rotulo_de_y=ry)
