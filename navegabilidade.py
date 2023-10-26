from funcoes import (
    calc_imc,
    ler_float,
    ler_int,
    ler_sexo,
    ler_str,
    limpa_tela,
    print_aluno,
    proximo_id,
    salvar,
)


def print_menu():
    menu = """
Opções:
1. Cadastrar novo aluno
2. Imprimir lista de alunos
3. Buscar aluno por id
4. Filtrar alunos por IMC
5. Configurações
6. Salvar dados e sair
"""
    print(menu)


def cadastrar(arq):
    alunos = arq["alunos"]
    while True:
        limpa_tela()
        print("Cadastrando novo aluno... Para cancelar digite 'sair'.\n")

        id_aluno = proximo_id(alunos)
        nome = ler_str("Digite o nome do aluno: ")
        if nome.lower() == "sair":
            return arq
        sexo = ler_sexo("Digite o sexo (Masc, Fem, Nao binario): ")
        peso = ler_float("Digite o peso em Kg: ")
        altura = ler_float("Digite a altura em METROS: ")
        imc = calc_imc(peso, altura)
        mensalidade = ler_float("Digite a mensalidade: ")

        aluno = {
            "id": id_aluno,
            "nome": nome,
            "sexo": sexo,
            "peso": peso,
            "altura": altura,
            "IMC": imc,
            "mensalidade": mensalidade,
        }
        alunos.append(aluno)
        arq[alunos] = alunos
        salvar(arq)

        print("\nAluno cadastrado com sucesso!")
        sair = input(
            "\nPara cadastrar outro aluno digite 'C', para sair aperte 'ENTER': "
        ).lower()
        if sair != "c":
            return arq


def listar_alunos(arq):
    # Mostra uma lista com todos os alunos cadastrados
    limpa_tela()
    alunos = arq["alunos"]
    print_aluno(arq, list(range(len(alunos))))


def busca_id(arq):
    # Faz uma busca usando um ID
    limpa_tela()

    alunos = arq["alunos"]

    print("Busca de aluno por ID")
    id_aluno = ler_int("Digite o ID: ")
    if id_aluno == -1:
        return
    while True:
        limpa_tela()
        print("\nBuscando...")
        for item in alunos:
            if item.get("id") == id_aluno:
                print("Aluno encontrado!\n")
                print_aluno(arq, id_aluno)
                break
        else:
            print("Aluno não encontrado. Verifique o número e tente novamente.\n")

        id_aluno = ler_int("Digite outro ID ou aperte 'ENTER' para sair: ")
        if id_aluno == -1:
            break


def filtro_imc():
    # Mostra todos os alunos com um IMC específico
    limpa_tela()
    print("Filtrando...")
    input("Para continuar aperte 'ENTER'")


def configuracoes(arq):
    config = arq["config"]

    alunos_pag = config["alunos_por_pag"]

    while True:
        limpa_tela()
        print(f"1. Alunos por página: {alunos_pag}")

        opc = ler_int("\nDigite o número para editar ou aperte 'ENTER' para sair: ")
        if opc == 1:
            alunos_pag = ler_int("Digite a quantidade de alunos por página: ")

        elif opc == -1:
            config["alunos_por_pag"] = alunos_pag
            arq["config"] = config
            return arq

        else:
            print("Opção inválida! Tente novamente.")
