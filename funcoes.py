"""
Funções gerais para uma aplicação de console como limpar a tela e imprimir o cabeçalho
"""
import os
import json
from math import ceil


if __name__ == "__main__":
    from main import sys_fitness

    sys_fitness()


def limpa_tela():
    """Limpa o console e imprime o cabeçalho do programa."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print_cabecalho()


def print_cabecalho():
    """Imprime o cabeçalho do programa"""
    cabecalho = """
  ************************************************************
  *                        SysFitness                        *
  ************************************************************
  """
    print(cabecalho)


def print_aluno(arq: dict, lista_impressao: int | list):
    """Imprime os dados de um ou mais alunos.

    Entradas:
    - `arq`: Recebe o dicionário que contém todos os alunos e configurações do aplicativo
    - `lista_impressao`: Número inteiro ou lista de IDs que será impressa no console.

    Obs: no caso de uma lista de alunos, a visualização será separada em páginas com qtd de alunos
    por página definida na configuração do arquivo `arq`.
    """
    alunos = arq["alunos"]

    if isinstance(lista_impressao, int):  # Se a 'lista_impressão' for um inteiro
        for item in alunos[lista_impressao]:  # Imprime cada item do dicionário
            print(f"{item.capitalize()}: {alunos[lista_impressao][item]}")
        print("\n**************************************************************\n")

    elif isinstance(lista_impressao, list):  # Se for uma lista
        config = arq["config"]

        # Prepara para a visualização em páginas
        alunos_pag = config["alunos_por_pag"]
        qtd_alu = len(lista_impressao)
        qtd_pag = ceil(qtd_alu / alunos_pag)
        pag_atual = 1

        while True:
            comeco_pag = (pag_atual - 1) * alunos_pag  # Primeiro item da página
            fim_pag = comeco_pag + (alunos_pag - 1)  # Último item da página

            limpa_tela()
            print(f"Mostrando a página {pag_atual} de {qtd_pag}\n")
            try:
                # Mostra do primeiro ao último item da página
                for i in range(comeco_pag, fim_pag + 1):
                    print_aluno(arq, lista_impressao[i])

            except IndexError:  # Caso não tenha mais nenhum item
                print("Fim da lista!\n")

            pag_atual = ler_pag(qtd_pag)
            if pag_atual == -1:
                break


def ler_int(msg="Digite um número: ", pos=False):
    """Lê uma string contendo um número Inteiro e retorna ele.

    Argumentos:
    - `msg`: Mensagem a ser visualizada ao pedir o número.
    - `pos`: 'positivo', define se o número a ser lido deve ser estritamente positivo

    """
    while True:
        num = input(msg)
        if num == "":
            return -1

        try:
            num = int(num)
            if pos and num < 0:
                print("O valor digitado deve ser maior que zero.")
                continue
            return num

        except ValueError:
            print("Valor inválido! Tente novamente.")


def ler_float(msg="Digite um número: ", pos=False):
    """Lê uma string contendo um número Real e retorna ele.

    Argumentos:
    - `msg`: Mensagem a ser visualizada ao pedir o número.
    - `pos`: 'positivo', define se o número a ser lido deve ser estritamente positivo

    """
    while True:
        num = input(msg)
        if num == "":
            return -1

        try:
            num = float(num)
            if pos and num < 0:
                print("O valor digitado deve ser maior que zero.")
                continue

            return num

        except ValueError:
            print("Valor inválido! Tente novamente.")


def ler_str(msg="Digite: ", sair=False):
    """Lê uma string não vazia e retorna ela.

    Entradas:
    - `msg`: Mensagem a ser mostrada ao pedir o texto.
    - `sair`: Se ao apertar 'ENTER' sem ter escrito nada deve-se retornar `-1`.

    """
    while True:
        texto = input(msg)
        if texto != "":
            return texto
        else:
            if sair:
                return -1
            else:
                print("Entrada vazia! Digite algo.")


def ler_s_n(msg="Escolha (S/N): "):
    """Retorna `True` se o usuário digitar 'sim' e `False` se digitar 'não'"""
    while True:
        opc = input(msg).lower()

        if opc in ["s", "sim"]:
            return True

        elif opc in ["n", "nao", "não"]:
            return False

        else:
            print("Opção inválida! Digite Sim(S) ou Não(N). ")


def ler_sexo(msg="Digite o sexo (M: Masculino, F: Feminino, NB: Não Binário): "):
    """Lê uma string que deve ser estritamente "masc", "fem" ou "nao binario" e a retorna."""
    while True:
        sexo = input(msg).lower()
        if sexo in ["m", "f", "nb"]:
            if sexo == "m":
                return "Masculino"

            elif sexo == "f":
                return "Feminino"

            elif sexo == "nb":
                return "Não binário"

        else:
            print("Valor inválido! Tente novamente.")


def ler_pag(qtd_pag: int, msg="Digite a página (ou aperte 'ENTER' para voltar): "):
    """Lê um número inteiro que esteja entre zero e a quantidade de páginas, caso nada
    for digitado, retorna `-1`.

    Entradas:
    - `qtd_pag`: Quantidade de páginas disponíveis para a escolha.
    - `msg`: Mensagem a ser mostrada ao pedir a página.

    """
    while True:
        pag = input(msg)
        if pag == "":
            return -1

        try:
            pag = int(pag)
        except ValueError:
            print(f"Valor inválido! Digite um número inteiro entre 1 e {qtd_pag}.")
            continue

        if pag < 1 or pag > qtd_pag:
            print(f"Página inválida! Digite um número entre 1 e {qtd_pag}.")
            continue
        else:
            return pag


def calc_imc(peso: float, altura: float):
    """Calcula o IMC a partir do peso e da altura,
    retorna o IMC com uma casa decimal."""
    imc = peso / (altura * altura)
    return float(f"{imc:.1f}")


def proximo_id(alunos: list):
    """Encontra o último ID encontrado na lista de alunos, adiciona 1 e retorna."""
    try:
        id_aluno = alunos[-1]["id"] + 1
        return id_aluno

    except IndexError:
        return 1


def busca_por_nome(arq: dict, nome: str):
    """Procura um nome na lista de alunos, se ele existir retorna o ID dele"""
    alunos = arq["alunos"]

    for item in alunos:
        if item["nome"].lower() == nome.lower():
            return item["id"]

    return -1


def carregar_alunos():
    """Carega as informações contidas no arquivo `alunos.json`. Caso o arquivo
    não exista, cria-se um novo automaticamente."""
    try:
        return json.load(open("alunos.json", mode="r", encoding="UTF-8"))

    except FileNotFoundError:
        novo = {"config": {"alunos_por_pag": 3}, "alunos": []}

        with open("alunos.json", mode="w", encoding="UTF-8") as outfile:
            json.dump(novo, outfile, indent=2)

        with open("alunos.json", mode="r", encoding="UTF-8") as arquivo:
            return json.load(arquivo)


def salvar(arq: dict):
    """Salva os dados em `alunos.json`"""
    with open("alunos.json", mode="w", encoding="UTF-8") as outfile:
        json.dump(arq, outfile, indent=2)
