from collections import deque
tdsing = [] # ingressos
idatual = 1
contatend = 0
tlog = 0 #contador 
tipos = ["VIP", "INTEIRA", "MEIA"]

def fazing(nome, tipo):
    global idatual
    if tipo not in tipos:
        return None, f"ERRO: Categoria '{tipo}' invalida."
    
    ing = {
        "id": idatual,
        "nome": nome,
        "tipo": tipo,
        "chegada": tlog,
        "inicioatend": None,
        "status": "PENDENTE"
    }
    idatual += 1
    return ing, None

def achaing(iding):
    for ing in tdsing:
        if ing['id'] == iding:
            return ing
    return None

def adding(ing):
    tdsing.append(ing)

def tiraing(iding):
    global tdsing
    tdsing = [ing for ing in tdsing if ing['id'] != iding]

def marcaatend(iding, tatend):
    global contatend
    ing = achaing(iding)
    if ing:
        ing['status'] = 'ATENDIDO'
        ing['inicioatend'] = tatend
        contatend += 1
        return True
    return False

def avancatempo():
    global tlog
    tlog += 1

def calcstats(fpadrao, fprior, modo):
    
    if modo == 'PADRAO':
        pend = list(fpadrao)
    else:
        pend = list(fprior['VIP']) + list(fprior['INTEIRA']) + list(fprior['MEIA'])

    totalpend = len(pend)
    atend = [ing for ing in tdsing if ing['status'] == 'ATENDIDO']
    contipo = {t: 0 for t in tipos}
    for ing in tdsing: contipo[ing['tipo']] += 1

    tespera = 0
    cespera = 0
    
    for ing in atend:
        if ing['inicioatend'] is not None:
            espera = ing['inicioatend'] - ing['chegada']
            tespera += espera
            cespera += 1
            
    mespera = tespera / cespera if cespera > 0 else 0.0

    return {
        "pend": totalpend,
        "atend": len(atend),
        "portipo": contipo,
        "mediaesp": round(mespera, 2)
    }
def pegaestadoing():
    return {
        'lista': [dict(ing) for ing in tdsing],
        'id': idatual,
        'contatend': contatend,
        'tempo': tlog
    }
def poeestadoing(estado):
    global tdsing, idatual, contatend, tlog
    tdsing = [dict(ing) for ing in estado['lista']]
    idatual = estado['id']
    contatend = estado['contatend']
    tlog = estado['tempo']