from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv


class Inventory:
    def type_date(path):

        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )

                products = []
                for row in csv_reader:
                    products.append(row)
            return products

    @staticmethod
    def import_data(path, type):
        products = Inventory.type_date(path)

        if type == "simples":
            return SimpleReport.generate(products)
        else:
            return CompleteReport.generate(products)
