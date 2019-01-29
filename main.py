# # from gate import Gate
# from toll import Toll
# from park import Park


# TESTE TOLL ________________________________________

# from dbToll import DBToll
# dbp = DBToll()

# from utils import Utils
# uts = Utils()

# t = Toll("Mauro","VW","GOL","vermelho","ZXC1234")
# dbp.UPDATE(t)
# dbp.CREATE(t)

# TESTE PARK ________________________________________

from infraPark import InfraPark
dbp = InfraPark()

from utils import Utils
uts = Utils()

# uts.newQR("joao", "qrcode")

t = Park("ZXC1234")
dbp.CREATE(t)


#pagar______________________________

# from dbPark import DBPark
# dbT = DBPark()

# from servicePark import servicePark
# client = servicePark(dbT)
# # patio = client.ENTRAR("BET01234")
# patio = client.SAIR("BET01234")

# TESTE CITY__________________________________________

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# cred = credentials.Certificate('serviceAccountKey.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# from city import City

# cities_ref = db.collection(u'cities')
# cities_ref.document(u'SF').set(
# City(u'San Francisco', u'CA', u'USA', False, 860000).to_dict())


#TESTE TIME_____________________________________

# import time

# inicio = time.time()
# time.sleep( 120 )
# fim = time.time()
# print(fim - inicio)
# print(((fim - inicio) / 60 )*2.5)

# import time
# inicio = 1545872400
# fim = 1545874200
# print(((fim - inicio) / 60 )*2.56)


#_____________________________________
# from dbToll import DBToll
# dbT = DBToll()

# from serviceToll import serviceToll
# client = serviceToll(dbT)
# client.ADDPASSAGEM("ZXC1234","Caxias", 11.50)