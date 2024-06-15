from caixa import login, criar_conta, criar_cliente, listar_contas
from caixa import menu, depositar, sacar, exibir_extrato


def main():
    clientes = []
    contas = []
    cliente_logado = None

    while True:
        opcao = menu(cliente_logado)

        if cliente_logado:
            if opcao == 1:
                depositar(cliente_logado)

            elif opcao == 2:
                sacar(cliente_logado)

            elif opcao == 3:
                exibir_extrato(cliente_logado)

        if opcao == 4:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            clientes.append(criar_cliente(clientes))

        elif opcao == 7:
            cliente_logado = login(clientes)

        elif opcao == 0:
            break


main()
