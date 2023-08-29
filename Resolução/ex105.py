def notas(*n, sit=False):
    """
    -> Funçaõ para analisar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    resp = {"total": len(n), "maior": max(n), "menor": min(n), "média": sum(n)/len(n)}
    if sit:
        if resp["média"] >= 7:
            resp["situação"] = "APROVADO"
        elif resp["média"] >= 5:
            resp["situação"] = "RECUPERAÇÃO"
        else:
            resp["situação"] = "REPROVADO"
    return resp


#Programa principal
resp = notas(3.5, 9, 6.5, sit=False)
print(resp)
help(notas)