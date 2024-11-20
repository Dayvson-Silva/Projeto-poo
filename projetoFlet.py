import flet as ft


class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


class Reserva:
    def __init__(self, cliente, data_entrada, data_saida, quarto):
        self.cliente = cliente
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quarto = quarto


class GerenciadorReservas:
    def __init__(self):
        self.reservas = []

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)


def main(page: ft.Page):
    page.title = "Hotel do Biu"
    page.scroll = "auto"

    gerenciador = GerenciadorReservas()

    # Widgets para capturar dados
    nome_input = ft.TextField(label="Nome")
    cpf_input = ft.TextField(label="CPF")
    telefone_input = ft.TextField(label="Telefone")
    data_entrada_input = ft.TextField(label="Data de Entrada (DD/MM/AAAA)")
    data_saida_input = ft.TextField(label="Data de Saída (DD/MM/AAAA)")

    # Quarto selecionado
    quarto_selecionado = ft.Dropdown(
        label="Escolha o quarto",
        options=[
            ft.dropdown.Option("Biu Normal"),
            ft.dropdown.Option("Biu Mega"),
            ft.dropdown.Option("Biu Premium"),
            ft.dropdown.Option("Biu Plus"),
        ],
    )

    # Lista de reservas
    lista_reservas = ft.ListView(expand=True, spacing=10)

    # Função para adicionar reserva
    def adicionar_reserva(e):
        if (
            nome_input.value
            and cpf_input.value
            and telefone_input.value
            and data_entrada_input.value
            and data_saida_input.value
            and quarto_selecionado.value
        ):
            cliente = Cliente(
                nome_input.value, cpf_input.value, telefone_input.value
            )
            reserva = Reserva(
                cliente,
                data_entrada_input.value,
                data_saida_input.value,
                quarto_selecionado.value,
            )
            gerenciador.adicionar_reserva(reserva)

            # Exibe a reserva na lista
            lista_reservas.controls.append(
                ft.Text(
                    f"Reserva para {cliente.nome} - Quarto: {quarto_selecionado.value} "
                    f"({data_entrada_input.value} a {data_saida_input.value})"
                )
            )
            lista_reservas.update()

            # Limpa os campos
            nome_input.value = ""
            cpf_input.value = ""
            telefone_input.value = ""
            data_entrada_input.value = ""
            data_saida_input.value = ""
            quarto_selecionado.value = None
            page.update()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha todos os campos!"), bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Text("Hotel do Biu - Sistema de Reservas", size=20, weight="bold"),
                nome_input,
                cpf_input,
                telefone_input,
                data_entrada_input,
                data_saida_input,
                quarto_selecionado,
                ft.ElevatedButton("Adicionar Reserva", on_click=adicionar_reserva),
                ft.Divider(),
                ft.Text("Reservas cadastradas:", size=16, weight="bold"),
                lista_reservas,
            ],
            expand=True,
            spacing=20,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
