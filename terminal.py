from ingressos import (fazing, adding, achaing, tiraing, tipos, calcstats)
from fila import (enfila, desenfila, espiar, listafila, removefila, mudamodo, migrapropri, migrapropadrao, pegamodo, fp, fpri)
from roteiro import vaipra, volta, avanca, onde, desenhamapa
from pilha import registraacao, desfazer, refazer, pegafotogeral

def mostraajuda():
    print("ajuda : comandos disponíveis:")
    print("fila & ingressos:")
    print("  comprar <nome> <tipo> : adquire ingresso (tipos: VIP, INTEIRA, MEIA). ex: comprar joao vip")
    print("  entrar : processa o próximo da fila.")
    print("  espiar : mostra o próximo da fila.")
    print("  cancelar <id> : cancela um ingresso pelo id. ex: cancelar 101")
    print("  listar : exibe a fila atual.")
    print("  estatisticas : mostra dados da fila.")
    print("  modo <padrao|prioridade> : altera o modo da fila. ex: modo prioridade")
    print("mapa & roteiro:")
    print("  ir <destino> : move o mapa. ex: ir palcoprincipal")
    print("  voltar : volta para a localização anterior.")
    print("  avancar : refaz o último avanço.")
    print("  onde : mostra a localização atual.")
    print("  mapa : desenha o mapa.")
    print("histórico:")
    print("  desfazer : desfaz a última ação.")
    print("  refazer : refaz a última ação desfeita.")
    print("geral: ajuda, sair")

def get_erro_uso(comando, uso_correto, descricao):
    return f"erro: comando {comando}. {descricao} uso correto: {uso_correto}"
def cmdcompra(a):
    if len(a) != 2:
        return get_erro_uso("comprar", "comprar <nome> <tipo>", "requer nome do cliente e tipo de ingresso.")
    nome, tipo = a
    ing, erro = fazing(nome, tipo.upper())
    if erro:
        tipos_validos = ", ".join(tipos)
        return get_erro_uso("comprar", "comprar <nome> <tipo>", f"tipo '{tipo.upper()}' inválido. tipos aceitos: {tipos_validos}.")
    fotoantiga = pegafotogeral()
    adding(ing)
    enfila(ing)
    registraacao("COMPRAR", fotoantiga)
    return f"ok: ingresso {ing['id']} ({ing['tipo']}) comprado para {ing['nome']}."
def cmdentrar():
    fotoantiga = pegafotogeral()
    ing = desenfila()
    if ing:
        registraacao("ENTRAR", fotoantiga)
        return f"entrou: ingresso {ing['id']} de {ing['nome']} ({ing['tipo']}). chegada em {ing['chegada']}min."
    return "fila vazia."
def cmdespiar():
    ing = espiar()
    return f"próximo: ingresso {ing['id']} de {ing['nome']} ({ing['tipo']}) chegada: {ing['chegada']}min." if ing else "fila vazia."

def cmdcancelar(a):
    if len(a) != 1 or not a[0].isdigit():
        return get_erro_uso("cancelar", "cancelar <id>", "requer um único id numérico.")
    iding = int(a[0])
    ing = achaing(iding)
    if not ing: 
        return get_erro_uso("cancelar", "cancelar <id>", f"ingresso com id {iding} não encontrado.")
    if ing['status'] != 'PENDENTE': 
        return get_erro_uso("cancelar", "cancelar <id>", f"ingresso {iding} não pode ser cancelado. status atual é {ing['status']} (apenas PENDENTE pode ser cancelado).")
    fotoantiga = pegafotogeral()
    removido = removefila(iding)
    if removido:
        tiraing(iding)
        registraacao("CANCELAR", fotoantiga)
        return f"ok: ingresso {iding} cancelado."
    return get_erro_uso("cancelar", "cancelar <id>", f"ingresso {iding} encontrado, mas falha ao remover da fila.")
def cmdlistar():
    lista = listafila(); modo = pegamodo()
    if not lista: return f"fila (modo: {modo}) está vazia."
    def _il(ing):
        return f"[{ing['id']}] {ing['nome']} ({ing['tipo']}) chg:{ing['chegada']}min"
    saida = [f"fila (modo: {modo}): {len(lista)} ingressos esperando"]
    if modo == 'PRIORIDADE':
        for t in tipos:
            ingst = [ing for ing in lista if ing['tipo'] == t]
            if ingst:
                saida.append(f"  > {t}: " + ", ".join([_il(ing) for ing in ingst]))
    else:
        saida.append("  > ordem de chegada: " + ", ".join([_il(ing) for ing in lista]))
    return '\n'.join(saida)
def cmdstats():
    stats = calcstats(fp, fpri, pegamodo())
    return (f"stats: pendentes={stats['pend']}, atendidos={stats['atend']} : "
            f"vip:{stats['portipo']['VIP']}, int:{stats['portipo']['INTEIRA']}, meia:{stats['portipo']['MEIA']} : "
            f"média de espera: {stats['mediaesp']:.2f}min")
def cmdmodo(a):
    opcoes = ['PADRAO', 'PRIORIDADE']
    if len(a) != 1 or a[0].upper() not in opcoes:
        return get_erro_uso("modo", "modo <padrao|prioridade>", f"o modo deve ser um de: {', '.join(opcoes).lower()}.")
    novom = a[0].upper(); modoa = pegamodo()
    if novom == modoa: return f"info: já está no modo '{novom.lower()}'."
    fotoantiga = pegafotogeral()
    if novom == 'PRIORIDADE': migrapropri()
    elif novom == 'PADRAO': migrapropadrao()
    mudamodo(novom)
    registraacao("MODO", fotoantiga)
    return f"ok: modo da fila alterado para '{novom.lower()}'."
def cmdir(a):
    if len(a) != 1: 
        return get_erro_uso("ir", "ir <destino>", "requer um único nome de destino.")
    c = a[0]
    fotoantiga = pegafotogeral()
    sucesso, res = vaipra(c)
    if sucesso:
        registraacao("IR", fotoantiga)
        return f"ok: roteiro atualizado. você está em {res.lower()}."
    return get_erro_uso("ir", "ir <destino>", f"falha ao ir para '{c}': {res}")
def cmdvolta():
    fotoantiga = pegafotogeral()
    sucesso, res = volta()
    if sucesso:
        registraacao("VOLTAR", fotoantiga)
        return f"ok: você voltou para {res.lower()}."
    return get_erro_uso("voltar", "voltar", "não há locais anteriores para voltar.")
def cmdavanca():
    fotoantiga = pegafotogeral()
    sucesso, res = avanca()
    if sucesso:
        registraacao("AVANCAR", fotoantiga)
        return f"ok: você avançou para {res.lower()}."
    return get_erro_uso("avancar", "avancar", "não há movimentos de roteiro para refazer/avançar.")
def cmonde(): 
    return f"localização atual: {onde().lower()}"  
def cmdmapa(): 
    print("mapa atual :")
    mapa = desenhamapa()
    return mapa if mapa else "mapa indisponível ou vazio."

def cmddesfazer():
    sucesso, res = desfazer()
    return f"desfazer: {res.lower()}" if sucesso else get_erro_uso("desfazer", "desfazer", f"falha ao desfazer: {res}")

def cmdrefazer():
    sucesso, res = refazer()
    return f"refazer: {res.lower()}" if sucesso else get_erro_uso("refazer", "refazer", f"falha ao refazer: {res}")

def main():
    cmds = {
        "AJUDA": mostraajuda, "COMPRAR": cmdcompra, "ENTRAR": cmdentrar, "ESPIAR": cmdespiar, 
        "CANCELAR": cmdcancelar, "LISTAR": cmdlistar, "ESTATISTICAS": cmdstats, "MODO": cmdmodo, 
        "IR": cmdir, "VOLTAR": cmdvolta, "AVANCAR": cmdavanca, "ONDE": cmonde, 
        "MAPA": cmdmapa, "DESFAZER": cmddesfazer, "REFAZER": cmdrefazer
    }
    print("olá! sistema de festival iniciado.")
    print("digite 'ajuda' para comandos ou 'sair' para finalizar.")
    mostraajuda()
    while True:
        try: 
            e = input("festival> ").strip()
        except EOFError: 
            break
        if not e: continue
        partes = e.split(); 
        c_upper = partes[0].upper();
        c_lower = partes[0].lower();
        a = partes[1:]
        if c_lower == "sair":
            print("sistema encerrado.")
            break
        if c_upper in cmds:
            func = cmds[c_upper]
            if c_upper in ["COMPRAR", "CANCELAR", "MODO", "IR"]: 
                res = func(a) 
            else: 
                res = func()
            if res: 
                print(res)
        else: 
            print(get_erro_uso(c_lower, "ajuda", f"comando '{c_lower}' desconhecido. digite AJUDA para a lista completa."))

if __name__ == "__main__":
    main()