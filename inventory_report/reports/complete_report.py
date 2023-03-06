from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def stocked_products(e, dict):
        output_stoked = "Produtos estocados por empresa:\n"
        for enterprise, amount in dict.items():
            output_stoked += f"- {enterprise}: {amount}\n"

        return output_stoked

    @classmethod
    def generate(e, parameter):
        method = super().generate(parameter)
        products = {}
        for dict in parameter:
            if not dict["nome_da_empresa"] in products:
                products[dict["nome_da_empresa"]] = 1
            else:
                products[dict["nome_da_empresa"]] += 1

        method += f"\n{e.stocked_products(products)}"
        return method
