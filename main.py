""" 
Projeto:
- Autor: Rafael Herrera
- GitHub: https://github.com/Redspe/SysFitness

Objetivo:
Considere um sistema de academia que organize e
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

from funcoes import carregar_alunos, ler_int, limpa_tela, salvar
from navegabilidade import (
    busca_id,
    busca_nome,
    cadastrar,
    configuracoes,
    filtro_imc,
    listar_alunos,
    print_menu,
)


def sys_fitness():
    """Executa o programa principal"""

    # Carregar alunos do arquivo
    arq = carregar_alunos()

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
            # Buscar aluno por ID
            busca_id(arq)

        elif opc == 4:
            # Buscar aluno por NOME
            busca_nome(arq)

        elif opc == 5:
            # Filtrar alunos por IMC
            filtro_imc(arq)

        elif opc == 6:
            # Abrir página de configurações
            arq = configuracoes(arq)

        elif opc == 7:
            # Salvar a lista de alunos
            salvar(arq)
            break

        else:
            print("\nOpção inválida! Escolha um dos números acima.")
            input("\nPara continuar aperte 'ENTER'")


if __name__ == "__main__":
    sys_fitness()
