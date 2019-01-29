import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from park import Park

from utils import Utils
uts = Utils()

class DBPark:

    def __init__(self):
        self.db = self.connect()
        self.collection = 'estacionamento'

    def connect(self):
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred)
        client = firestore.client()
        return client
    
    def CREATE(self,obj):
        doc_ref = self.db.collection(uts.codificar(self.collection)).document(uts.codificar(obj.placa.upper())).set(obj.to_dict())

    def READ(self, placa):
        doc_ref = self.db.collection(uts.codificar(self.collection)).document(uts.codificar(placa.upper()))
        doc = doc_ref.get()
        obj = Park.from_dict(doc.to_dict())
        return obj

    def READ_ALL(self):
        doc_ref = self.db.collection(uts.codificar(self.collection))
        docs = doc_ref.get()
        carros = list()
        for doc in docs:
            carros.append(Park.from_dict(doc.to_dict()))
        return carros

    def UPDATE(self, obj):
        doc_ref = self.db.collection(uts.codificar(self.collection)).document(uts.codificar(obj.placa.upper()))
        doc_ref.update(obj.to_dict())
                   
    def DELETE(self, placa):
        self.db.collection(uts.codificar(self.collection)).document(uts.codificar(placa.upper())).delete()

    def DELETE_FIELD(self, campo, placa):
        doc_ref = self.db.collection(uts.codificar(self.collection)).document(uts.codificar(placa.upper()))
        doc_ref.update({uts.codificar(campo): firestore.DELETE_FIELD})
