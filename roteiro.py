localatual = "/"
v = [] # volta
a = [] # vai
lugares = {
    "/": "entrada",
    "/P": "Palco",
    "/AA": "Area",
    "/AA/V": "Vale",
    "/R": "robotica",
}

def resolvecaminho(c):
    global localatual
    if c.startswith('/'): cfinal = c
    else:
        if f"/{c}" in lugares: cfinal = f"/{c}"
        else: cfinal = f"{localatual}/{c}"
    if cfinal in lugares: return cfinal
    return None
def vaipra(c):
    global localatual, v, a
    novo = resolvecaminho(c)
    if novo:
        if novo != localatual:
            v.append(localatual) 
            a = [] 
            localatual = novo
            return True, novo
        else: return True, novo 
    
    return False, f"ERRO: nao existe."

def volta():
    global localatual, v, a
    if not v: return False, "Nao da pra voltar mais."
    a.append(localatual) 
    localatual = v.pop() 
    return True, localatual
def avanca():
    global localatual, v, a
    if not a: return False, 
    v.append(localatual)
    localatual = a.pop() 
    return True, localatual
def onde():
    return localatual
def desenhamapa():
    s = "onde foi\n"
    s += "(VOLTAR):\n"
    if v:
        for i, l in enumerate(reversed(v)): s += f"  {len(v) - i}. {l} ({lugares.get(l, 'Desconhecido')})\n"
    else: s += "  (Vazio)\n"
    s += f"\nLocal Atual:\n"
    s += f"  -> {localatual} ({lugares.get(localatual, 'entrada')})\n"
    s += "\nProximos (AVANCAR):\n"
    if a:
        for i, l in enumerate(reversed(a)): s += f"  {len(a) - i}. {l} ({lugares.get(l, 'Desconhecido')})\n"
    else: s += "  (Vazio)\n"
    return s
def pegaestadomapa():
    return {
        'local': localatual,
        'v': list(v),
        'a': list(a)
    }
def poeestadomapa(estado):
    global localatual, v, a
    localatual = estado['local']
    v = estado['v']
    a = estado['a']