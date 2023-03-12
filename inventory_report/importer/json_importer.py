from .importer import Importer
import json


# Classe herdeira de Importer
class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            return list(json.load(file))
