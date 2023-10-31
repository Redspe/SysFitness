"""
Contém as funções necessárias para os menus e 
a navegabilidade geral do sistema.
"""
import time
from funcoes import (
    calc_imc,
    ler_float,
    ler_int,
    ler_s_n,
    ler_sexo,
    ler_str,
    limpa_tela,
    busca_por_nome,
    print_aluno,
    proximo_id,
    salvar,
)

if __name__ == "__main__":
    from main import sys_fitness

    sys_fitness()


def print_menu():
    """Imprime o menu principal e suas opções"""
    menu = """
Opções:
1. Cadastrar novo aluno
2. Mostrar lista de alunos
3. Buscar aluno por ID
4. Buscar aluno por NOME
5. Filtrar alunos por IMC

6. Configurações

7. Salvar dados e sair
"""
    print(menu)


def cadastrar(arq):
    """Faz o cadastro de novos alunos"""
    alunos = arq["alunos"]
    while True:

        def cadastro():
            limpa_tela()
            print("Cadastrando novo aluno... Para cancelar digite 'sair'.\n")

            id_aluno = proximo_id(alunos)
            nome = ler_str("Digite o nome do aluno: ", sair=True)
            if nome == -1:
                return arq

            busca = busca_por_nome(arq, nome)
            if busca != -1:
                ver = ler_s_n(
                    "\nEste nome já está cadastrado. Gostaria de visualizar (S/N)? "
                )
                print()
                if ver:
                    print_aluno(arq, busca)

                opc = ler_s_n("Deseja continuar o cadastro? (S/N): ")
                print()
                if opc:
                    return arq

            sexo = ler_sexo(
                "Digite o sexo (M: Masculino, F: Feminino, NB: Não Binário): "
            )
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
            arq["alunos"] = alunos
            salvar(arq)

            print("\nAluno cadastrado com sucesso!")

        cadastro()

        sair = input(
            "\nPara cadastrar outro aluno digite 'C', para sair aperte 'ENTER': "
        ).lower()
        if sair != "c":
            return arq


def listar_alunos(arq):
    """Mostra uma lista com todos os alunos cadastrados"""
    limpa_tela()
    alunos = arq["alunos"]
    print_aluno(arq, list(range(len(alunos))))


def busca_id(arq):
    """Faz uma busca usando um ID"""
    limpa_tela()

    alunos = arq["alunos"]

    print("Busca de aluno por ID")
    id_aluno = ler_int("Digite o ID: ", pos=True)
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
            time.sleep(1)
            print("Aluno não encontrado. Verifique o número e tente novamente.\n")

        id_aluno = ler_int("Digite outro ID ou aperte 'ENTER' para sair: ", pos=True)
        if id_aluno == -1:
            break


def busca_nome(arq):
    """Item do menu para busca de um aluno a partir do nome"""
    limpa_tela()

    print("Busca de aluno por NOME")
    nome_aluno = ler_str("Digite o NOME ou aperte 'ENTER' para sair: ", sair=True)
    if nome_aluno == -1:
        return

    while True:
        limpa_tela()
        print("\nBuscando...")

        id_resposta = busca_por_nome(arq, nome_aluno)
        if id_resposta != -1:
            print("Aluno encontrado!\n")
            print_aluno(arq, id_resposta)

        else:
            time.sleep(1)
            print("Aluno não encontrado. Verifique o nome e tente novamente.\n")

        nome_aluno = ler_str("Digite outro NOME ou aperte 'ENTER' para sair: ", sair=True)
        if nome_aluno == -1:
            break


def filtro_imc(arq):
    """Mostra todos os alunos com um IMC específico"""
    alunos = arq["alunos"]

    while True:
        limpa_tela()
        print("Pesquisa de alunos por IMC\n")

        imc = ler_float("Digite o IMC ou aperte 'ENTER' para sair: ", pos=True)

        if imc != -1:
            al_filtrados = [item["id"] for item in alunos if item["IMC"] >= imc]
            print_aluno(arq, al_filtrados)

        else:
            return


def configuracoes(arq):
    """Mostra uma página com as configurações do app"""
    config = arq["config"]

    alunos_pag = config["alunos_por_pag"]

    while True:
        limpa_tela()
        print(f"1. Alunos por página: {alunos_pag}")

        opc = ler_int(
            "\nDigite '1' para editar ou aperte 'ENTER' para sair: ", pos=True
        )
        if opc == 1:
            alunos_pag = ler_int("Digite a quantidade de alunos por página: ", pos=True)

        elif opc == -1:
            config["alunos_por_pag"] = alunos_pag
            arq["config"] = config
            return arq

        else:
            print("Opção inválida! Tente novamente.")
