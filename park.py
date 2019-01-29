from utils import Utils
uts = Utils()

import time

class Park(object):
    def __init__(self, placa, entrada=time.time(), saida=None, valor=None, pago=False):
        self.placa = placa.upper()
        self.entrada = entrada
        self.saida = saida
        self.valor = valor
        self.pago = pago

    @staticmethod
    def from_dict(source):
        park = Park(source[u'placa'], source[u'entrada'],source[u'pago'])
        if u'saida' in source:
            park.saida = source[u'saida']
        if u'valor' in source:
            park.valor = source[u'valor']
        return park

    def to_dict(self):
        dest = {
            u'placa': uts.codificar(self.placa),
            u'entrada':self.entrada,
            u'pago':self.pago
        }
        if self.saida:
            dest[u'saida'] = self.saida
        if self.valor:
            dest[u'valor'] = self.valor
        return dest

    def __repr__(self):
        return u'Park(placa={}, entrada={}, saida={}, valor={}, pago={})'.format(
            self.placa, self.entrada, self.saida, self.valor,self.pago)