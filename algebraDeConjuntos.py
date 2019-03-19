
def uniao(conj1, conj2):
    listaResultado = []
    for a in conj1:
        listaResultado.append(a)
    for a in conj2:
        if a not in listaResultado:
            listaResultado.append(a)
    return listaResultado

def interseccao(conj1, conj2):
    listaResultado = []
    for a in conj1:
        if a in conj2:
            listaResultado.append(a)
    return listaResultado

def diferenca(conj1, conj2):
    listaResultado = []
    for a in conj1:
        if a not in conj2:
            listaResultado.append(a)
    return listaResultado


def produtoCartesiano(conj1, conj2):
    listaResultado = []
    aux = ''
    for a in conj1:
        for b in conj2:
            aux = ('({0},{1})'.format(a,b))
            listaResultado.append(aux)
    return listaResultado


def complemento(conjU, conj1):
    listaResultado = []
    for a in conjU:
        if a not in conj1:
            listaResultado.append(a)

    return listaResultado


def uniaoDisjunta(silva, sousa):
    listaResultado = []
    for a in silva:
        aux = []
        aux.append(a)
        aux.append('Silva')
        listaResultado.append(aux)
    for b in sousa:
        if b not in silva:
            aux = []
            aux.append(b)
            aux.append('Sousa')
            listaResultado.append(aux)
    return listaResultado


conj1 = [1, 2, 3, 4]
conj2 = [1, 2, 5, 6, 7]

silva = ['João', 'Maria', 'Jose']
sousa = ['Pedro', 'Ana', 'Jose']

resultado1 = uniao(conj1, conj2)
#print(resultado1)

resultado2 = interseccao(conj1, conj2)
#print(resultado2)

conjU = [1, 2, 3, 4, 5, 6]
resultado3 = complemento(conjU, conj1)
#print(resultado3)

resultado4 = diferenca(conj1, conj2)
#print(resultado4)

resultado5 = produtoCartesiano(conj1, conj2)
#print(resultado5)

resultado6 = uniaoDisjunta(silva, sousa)
#print(resultado6)
