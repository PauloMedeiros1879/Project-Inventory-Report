from inventory_report.inventory.product import Product

# Iniciando projeto! :D


def test_cria_produto():
    id = 0
    produto = "produto"
    empresa = "empresa"
    fabricacao = "fabricacao"
    validade = "validade"
    serie = "serie"
    armazenamento = "armazenamento"
    inventory = Product(
        id, produto, empresa, fabricacao, validade, serie, armazenamento
    )
    assert inventory.id == id
    assert inventory.nome_do_produto == produto
    assert inventory.nome_da_empresa == empresa
    assert inventory.data_de_fabricacao == fabricacao
    assert inventory.data_de_validade == validade
    assert inventory.numero_de_serie == serie
    assert inventory.instrucoes_de_armazenamento == armazenamento
