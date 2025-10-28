from ingressos import pegaestadoing, poeestadoing
from fila import pegaestadofila, poeestadofila
from roteiro import pegaestadomapa, poeestadomapa
d = [] # desfaz
r = [] # refaz

def pegafotogeral():
    return {
        'ing': pegaestadoing(),
        'fila': pegaestadofila(),
        'mapa': pegaestadomapa()
    }
def voltafotogeral(estado):
    poeestadoing(estado['ing'])
    poeestadofila(estado['fila'])
    poeestadomapa(estado['mapa'])
def registraacao(nomeacao, estadoantigo):
    global d, r
    d.append({'acao': nomeacao, 'estado': estadoantigo})
    r = [] 

def desfazer():
    global d, r
    
    if not d: return False,
    estadoatual = pegafotogeral()
    acao = d.pop()
    voltafotogeral(acao['estado'])
    r.append({'acao': acao['acao'], 'estado': estadoatual})
    return True, f"OK: Desfeito '{acao['acao']}'."

def refazer():
    global d, r
    if not r: return False,
    estadoatual = pegafotogeral()
    acao = r.pop()
    voltafotogeral(acao['estado'])
    d.append({'acao': acao['acao'], 'estado': estadoatual})
    return True, f"OK: Refeito '{acao['acao']}'."