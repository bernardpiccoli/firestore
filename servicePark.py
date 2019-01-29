from dbPark import DBPark
from park import Park
import json

from utils import Utils
uts = Utils()

class servicePark:

    def __init__(self, firestore):
        self.firestore = firestore
        self.tarifa = 4

    def ENTRAR(self, placaReferencia):
        self.firestore.CREATE(Park(placaReferencia))
        self.IMPRIMIR(uts.dataHoraAgora(), placaReferencia)

    def SAIR(self, placaReferencia):
        obj = self.firestore.READ(placaReferencia)
        obj.saida = uts.timestamp()
        self.PAGAR(obj)
        obj.valor = self.CALCULAR(obj.entrada, obj.saida, self.tarifa)
        self.firestore.UPDATE(obj)

    def IMPRIMIR(self, entrada, placaReferencia):
        uts.newQR(entrada, placaReferencia)

    def CALCULAR(self, entrada, saida, tarifa):
        tarifa_s = tarifa/3600.0
        permanencia = (saida - entrada) 
        valor = permanencia *tarifa_s
        return valor

    def PAGAR(self, obj):
        obj.pago = True

    def PATIO(self):
        obj = self.firestore.READ_ALL()
        return obj