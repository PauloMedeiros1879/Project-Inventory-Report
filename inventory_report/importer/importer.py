from abc import ABC, abstractmethod


# Classe Abstrata Importer().
class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls):
        raise NotImplementedError
