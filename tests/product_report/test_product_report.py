from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        12345002,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        987654321,
        "ao abrigo de luz",
    )

    result = product.__repr__()

    assert type(result) == str
    assert result == (
        "O produto farinha "
        "fabricado em 01-05-2021 "
        "por Farinini com validade "
        "até 02-06-2023 "
        "precisa ser armazenado ao abrigo de luz."
    )
