""" Considere um sistema de academia que organize e
armazene os seguintes dados dos alunos:
- id, nome, sexo, peso, altura, mensalidade.
- utiliza uma estrutura de lista de dicionários para
manter esses dados durante a execução

tenha as seguintes funcionalidades:

1. Cadastrar novo aluno
2. Imprimir lista de alunos
3. buscar aluno por id
4. filtrar alunos com imc > 30
5. Salvar dados e sair

● Implemente sempre que possível funções unitárias
○ ex:
■ Cadastrar um registro de aluno
■ imprimir um registro de aluno
■ etc.
"""

import json
from funcoes import ler_int, limpa_tela, salvar
from navegabilidade import (
    busca_id,
    cadastrar,
    configuracoes,
    filtro_imc,
    listar_alunos,
    print_menu,
)


def sys_fitness():
    """Executa o programa principal"""

    # Carregar alunos do arquivo
    arq = json.load(open("alunos.json", mode="r", encoding="UTF-8"))

    while True:
        limpa_tela()
        print_menu()
        opc = ler_int(pos=True)

        # Navegabilidade
        if opc == 1:
            # Cadastrar novo aluno
            arq = cadastrar(arq)

        elif opc == 2:
            # Imprimir lista de alunos
            listar_alunos(arq)

        elif opc == 3:
            # Buscar aluno por id
            busca_id(arq)

        elif opc == 4:
            # Filtrar alunos por IMC
            filtro_imc(arq)

        elif opc == 5:
            # Abrir página de configurações
            arq = configuracoes(arq)

        elif opc == 6:
            # Salvar a lista de alunos
            salvar(arq)
            break

        else:
            print("\nOpção inválida! Escolha um dos números acima.")
            input("\nPara continuar aperte 'ENTER'")


if __name__ == "__main__":
    sys_fitness()
