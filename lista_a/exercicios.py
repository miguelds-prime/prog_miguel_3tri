# Lista A - Miguel D. Silva (N 28, 1C)
# Respostas recuperadas do arquivo enviado pelo aluno (Codespaces sem cota).

# ---------- Bloco 1 ----------
def conta_negativos(lista):
    t = 0
    for a in lista:
        if a < 0:
            t += 1
    return t


def media(lista):
    if not lista:
        return 0

    s = 0
    for a in lista:
        s += a
    return s / len(lista)


def sem_o_maior(lista):
    if not lista:
        return []

    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n

    a = []
    ja_tirou = False
    for n in lista:
        if n == maior and not ja_tirou:
            ja_tirou = True
        else:
            a.append(n)
    return a


def acumulada(lista):
    a = []
    s = 0

    for n in lista:
        s += n
        a.append(s)
    return a


def achata(lista_de_listas):
    a = []
    for sublista in lista_de_listas:
        for item in sublista:
            a.append(item)
    return a


# ---------- Bloco 2 ----------
def busca_ultima(lista, alvo):
    p = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            p = i
    return p


def conta_ocorrencias(lista, alvo):
    t = 0
    for n in lista:
        if n == alvo:
            t += 1
    return t


def primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    p = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            p = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return p


# ---------- Bloco 3 ----------
def soma_pares_contando(lista):
    s = 0
    operacoes = 0

    for a in lista:
        operacoes += 1
        if a % 2 == 0:
            s += a
    return s, operacoes


def maior_contando(lista):
    if not lista:
        return None, 0
    maior = lista[0]
    comparacoes = 0

    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]

    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes

    return False, comparacoes


def ordenada_contando(lista):
    comparacoes = 0

    for a in range(len(lista) - 1):
        comparacoes += 1
        if lista[a] > lista[a + 1]:
            return False, comparacoes

    return True, comparacoes


# ---------- Bloco 4 ----------
def inverte_no_lugar(lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:

        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1

    return True


def par_que_soma(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        s = lista[inicio] + lista[fim]
        if s == alvo:
            return inicio, fim
        elif s < alvo:
            inicio += 1
        else:
            fim -= 1

    return -1, -1


def soma_maxima_janela(lista, k):
    if len(lista) < k or k <= 0:
        return 0

    s = sum(lista[:k])
    melhor = s

    for i in range(k, len(lista)):

        s = s + lista[i] - lista[i - k]
        if s > melhor:
            melhor = s

    return melhor


def parenteses_balanceados(texto):
    pilha = []
    pares = {')': '(', ']': '['}

    for char in texto:
        if char in "([":
            pilha.append(char)
        elif char in ")]":
            if not pilha:
                return False
            topo = pilha.pop()
            if topo != pares[char]:
                return False

    return len(pilha) == 0
