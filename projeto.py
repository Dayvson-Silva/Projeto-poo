

class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco

class Reserva:
    def __init__(self, cliente, data_entrada, data_saida):
        self.__cliente = cliente
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida

class GerenciadorReservas:
    def __init__(self):
        self.__reservas = []

    def adicionar_reserva(self, reserva):
        self.__reservas.append(reserva)
        print("Reserva adicionada com sucesso!")

def menu():
    print("------------- Hotel do Biu -------------")
    print("------------- BEM VINDOS -------------")
    print(" Escolha seu Quarto ")
    print("1. Biu Normal")
    print("2. Biu Mega")
    print("3. Biu Premium")
    print("4. Biu Plus")

    # Try: Envolve o código que pode gerar exceções
    try:
        opcao = int(input("Qual deseja: "))
        return opcao
    # o except serve para tratar a execeção. e o valueerror serve para tratar erros tipo recebendo um argumento correto com o valor invalido
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0

if __name__ == "__main__":
    gerenciador = GerenciadorReservas()

    while True:
        opcao = menu()
        if opcao in [1, 2, 3, 4]:
            print(f"Opção escolhida: {opcao}")
            nome = input("Digite seu Nome: ")
            cpf = input("Digite seu CPF: ")
            telefone = input("Digite seu Telefone: ")
            data_entrada = input("Digite sua Data de Entrada (formato: DD/MM/AAAA): ")
            data_saida = input("Digite sua Data de Saída (formato: DD/MM/AAAA): ")
            
            cliente = Cliente(nome, cpf, telefone)
            reserva = Reserva(cliente, data_entrada, data_saida)
            gerenciador.adicionar_reserva(reserva)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

       