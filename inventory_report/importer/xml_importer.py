from .importer import Importer
import xmltodict


# Classe herdeira de Importer
class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
