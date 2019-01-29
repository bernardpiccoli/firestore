from dbPark import DBPark
from toll import Toll
import json

class serviceToll:

    def __init__(self, firestore):
        self.firestore = firestore

    def ADDPASSAGEM(self, placaReferencia , local, valor):
        obj = self.firestore.READ(placaReferencia)
        print(obj)
        t = Toll(obj.proprietario, obj.marca, obj.modelo,  obj.cor, placaReferencia, obj.historico)
        t.PASSAR(local, valor)
        print("Passou")
        self.firestore.UPDATE(t)

    def OBTERPASSAGENS(self, placaReferencia):
        obj = self.firestore.READ_TOLL(placaReferencia)
        return obj
    
    def EXTRATOMENSAL():
        return 1