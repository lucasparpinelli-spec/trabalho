metas = []
# lucas ⬇️
def cadastrar_meta():
    nome = str(input("Digite o nome da meta: "))
    prazo = str(input("Digite o prazo da meta: "))
    categoria = str(input("Digite qual é a categoria Da Meta: "))
    prioridade = str(input("Digite a prioridade: "))

    meta = {
        "nome": nome,
        "prazo": prazo,
        "categoria": categoria,
        "prioridade": prioridade,
        "realizada": False
    }

    metas.append(meta)
    print("😁 Meta cadastrada com sucesso! 😁\n")

# lucas ⬇️
def consultar_meta():
    if len(metas) == 0:
        print("😅 Não há metas cadastradas! 😅\n")
        return

    num = 1
    for meta in metas:
        if meta["realizada"] == True:
            status = "✅ Realizada"
        else:
            status = "❌ Pendente"

        print(f"[{num}] Nome: {meta['nome']} | Prazo: {meta['prazo']} | "
              f"Categoria: {meta['categoria']} | Prioridade: {meta['prioridade']} | "
              f"Status: {status}")
        num += 1
    print()

# lucas ⬇️
def buscar_meta():
    buscar = str(input("Buscar por nome ou prazo: ")).lower()

    encontrados = []

    for meta in metas:
        if buscar in meta["nome"].lower() or buscar in meta["prazo"].lower():
            encontrados.append(meta)

    if len(encontrados) == 0:
        print("❌ Não encontrado! 😥\n")
        return

    num = 1
    for meta in encontrados:
        if meta["realizada"] == True:
            status = "✅ Realizada"
        else:
            status = "❌ Pendente"

        print(f"[{num}] Nome: {meta['nome']} | Prazo: {meta['prazo']} | "
              f"Categoria: {meta['categoria']} | Prioridade: {meta['prioridade']} | "
              f"Status: {status}")
        num += 1
    print()

# lucas ⬇️
def marcar_realizada():
    consultar_meta()

    if len(metas) == 0:
        return

    num = int(input("Digite o número da meta para marcar como realizada: "))
    indice = num - 1

    if 0 <= indice < len(metas):
        metas[indice]["realizada"] = True
        print("✅ Meta marcada como realizada! ✅\n")
    else:
        print("⚠️ Número inválido! ⚠️\n")

# lucas ⬇️
def atualizar_meta():
    consultar_meta()

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
# samay ⬇️
def exibir_menu():
    while True:
        print('=== Sistema de metas pessoais ===')
        print('1. Cadastrar nova meta')
        print('2. Consultar todas as metas')
        print('3. Buscar por tema ou dia')
        print('4. Marcar meta como realizada')
        print('5. Excluir meta')
        print('6. Atualizar meta')
        print('7. Sair')
        escolha = str(input('Escolha uma opção:'))
        if escolha == '1':
            cadastrar_meta()
        elif escolha == '2':
            consultar_meta()
        elif escolha == '3':
            buscar_meta()
        elif escolha == '4':
            marcar_realizada()
        elif escolha == '5':
            excluir_meta()
        elif escolha == '6':
            atualizar_meta()
        elif escolha == '7':
            print('Saindo do sistema. Até a Proxima!')
            break
        else:
            print('Opção invalida. Tente novamente.\n')
# samay ⬇️
def excluir_meta():
    consultar_meta()
    if len(metas) == 0:
        return
    else:
        numero = int(input('Digite o numero da meta para excluir :'))
        indice = numero - 1
        if 0 <= indice < len(metas):
            metas.pop(indice)
            print('meta excluida .\n')
        else:
            print('numero invalido.\n')

def iniciar_sistema():
     print("..... Sistema iniciando ....")
     print(" Olá Usuario insira como quer ser chamado: ")
     nome=str(input())
     print(f'Sejá bem vindo ao sistema {nome}')
     exibir_menu()
iniciar_sistema()