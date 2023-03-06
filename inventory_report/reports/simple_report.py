from abc import ABC
from datetime import datetime


class SimpleReport(ABC):
    @classmethod
    def convert_date(e, date):
        # mais sobre o método strptime()
        # https://www.programiz.com/python-programming/datetime/strptime
        return datetime.strptime(date, "%Y-%m-%d")

    @classmethod
    def generate(e, parameter):
        old = datetime.max
        nearest = datetime.max
        products = {}
        for dict in parameter:

            old = min(old, e.convert_date(dict["data_de_fabricacao"]))

            nearest = (
                min(nearest, e.convert_date(dict["data_de_validade"]))
                # date.today() método para obter a data local atual.
                if e.convert_date(dict["data_de_validade"]) > datetime.today()
                else nearest
            )

            if not dict["nome_da_empresa"] in products:
                products[dict["nome_da_empresa"]] = 1
            else:
                products[dict["nome_da_empresa"]] += 1

        return (
            f"Data de fabricação mais antiga: {old.date()}\n"
            f"Data de validade mais próxima: {nearest.date()}\n"
            f"Empresa com mais produtos: {max(products, key=products.get)}"
        )
