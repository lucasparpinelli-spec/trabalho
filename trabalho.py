metas = []

def cadastrar_meta():
    nome = str(input("Digite o nome da meta: "))
    prazo = str(input("Digite o prazo da meta: "))
    categoria = str(input("Digite qual é a categoria: "))
    prioridade = str(input("Digite a prioridade: "))

    meta = {
        "nome": nome,
        "prazo": prazo,
        "categoria": categoria,
        "prioridade": prioridade,
        "pendente": False
    }

    metas.append(meta)
    print("😁 Meta cadastrada com sucesso! 😁\n")


def consultar_metas():
    if len(metas) == 0:
        print("😅 Não há metas cadastradas! 😅\n")
        return

    num = 1
    for meta in metas:
        if meta["pendente"] == True:
            status = "✅ Realizada"
        else:
            status = "❌ Pendente"

        print(f"[{num}] Nome: {meta['nome']} | Prazo: {meta['prazo']} | "
              f"Categoria: {meta['categoria']} | Prioridade: {meta['prioridade']} | "
              f"Status: {status}")
        num += 1
    print()


def buscar_sessao():
    termo = str(input("Buscar por nome ou prazo: ")).lower()

    encontrados = []

    for meta in metas:
        if termo in meta["nome"].lower() or termo in meta["prazo"].lower():
            encontrados.append(meta)

    if len(encontrados) == 0:
        print("❌ Não encontrado! 😥\n")
        return

    num = 1
    for meta in encontrados:
        if meta["pendente"] == True:
            status = "✅ Realizada"
        else:
            status = "❌ Pendente"

        print(f"[{num}] Nome: {meta['nome']} | Prazo: {meta['prazo']} | "
              f"Categoria: {meta['categoria']} | Prioridade: {meta['prioridade']} | "
              f"Status: {status}")
        num += 1
    print()


def marcar_realizada():
    consultar_metas()

    if len(metas) == 0:
        return

    num = int(input("Digite o número da meta para marcar como realizada: "))
    indice = num - 1

    if 0 <= indice < len(metas):
        metas[indice]["pendente"] = True
        print("✅ Meta marcada como realizada! ✅\n")
    else:
        print("⚠️ Número inválido! ⚠️\n")
def atualizar_meta():
    consultar_metas()

    if len(metas) == 0:
        return

    num = int(input("Digite o número da meta que deseja atualizar: "))
    indice = num - 1

    if 0 <= indice < len(metas):
        metas[indice]["nome"] = input("Novo nome: ")
        metas[indice]["prazo"] = input("Novo prazo: ")
        metas[indice]["categoria"] = input("Nova categoria: ")
        metas[indice]["prioridade"] = input("Nova prioridade: ")

        print("✏️ Meta atualizada com sucesso! ✏️\n")
    else:
        print("⚠️ Número inválido! ⚠️\n")
