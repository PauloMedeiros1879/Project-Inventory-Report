from .importer import Importer
import csv


# Classe herdeira de Importer
class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            return list(csv.DictReader(file))
