from collections import deque
from ingressos import tipos, marcaatend, avancatempo, pegaestadoing
fp = deque()
fpri = {t: deque() for t in tipos} 
modo = 'PADRAO'

def pegamodo():
    return modo

def mudamodo(novom):
    global modo
    if novom in ['PADRAO', 'PRIORIDADE']:
        modo = novom
        return True
    return False

def migrapropri():
    global fp, fpri
    while fp:
        ing = fp.popleft()
        fpri[ing['tipo']].append(ing)
    return True

def migrapropadrao():
    global fp, fpri
    
    lista = []
    
    for t in tipos:
        while fpri[t]:
            lista.append(fpri[t].popleft())
            
    lista.sort(key=lambda x: x['chegada']) 
    
    for ing in lista:
        fp.append(ing)
    
    return True

def enfila(ing):
    if modo == 'PADRAO':
        fp.append(ing)
    else:
        fpri[ing['tipo']].append(ing)
        
def desenfila():  
    ing = None
    if modo == 'PADRAO':
        if fp:
            ing = fp.popleft()
    elif modo == 'PRIORIDADE':
        for t in tipos: 
            if fpri[t]:
                ing = fpri[t].popleft()
                break
    if ing:
        tatend = pegaestadoing()['tempo']
        avancatempo() 
        marcaatend(ing['id'], tatend) 
        return ing
    return None

def espiar():
    if modo == 'PADRAO':
        if fp: return fp[0]
            
    elif modo == 'PRIORIDADE':
        for t in tipos:
            if fpri[t]: return fpri[t][0]
                
    return None

def listafila():
    
    if modo == 'PADRAO':
        return list(fp)
        
    elif modo == 'PRIORIDADE':
        l = []
        for t in tipos: l.extend(list(fpri[t]))
        return l
        
    return []

def removefila(iding):
    achou = None
    if modo == 'PADRAO':
        temp = deque()
        while fp:
            ing = fp.popleft()
            if ing['id'] == iding: achou = ing
            else: temp.append(ing)
        fp.extend(temp)
        
    elif modo == 'PRIORIDADE':
        for t in tipos:
            temp = deque()
            while fpri[t]:
                ing = fpri[t].popleft()
                if ing['id'] == iding: achou = ing
                else: temp.append(ing)
            fpri[t].extend(temp)

    return achou
def pegaestadofila():
    return {
        'fp': deque(list(fp)),
        'fpri': {t: deque(list(fpri[t])) for t in tipos},
        'modo': modo
    }

def poeestadofila(estado):
    global fp, fpri, modo
    fp = estado['fp']
    fpri = estado['fpri']
    modo = estado['modo']