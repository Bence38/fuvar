class Fuvarok:
    def __init__(self, taxi_id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes_modja):
        self.taxi_id = taxi_id
        self.indulas = indulas
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo
        self.fizetes_modja = fizetes_modja
    def __str__(self):
        return f"Taxi azonosítója:{self.taxi_id} Indulás időpontja: {self.indulas} Utazás Időtartama: {self.idotartam} Megtett távolság: {self.tavolsag}  Viteldíj: {self.viteldij} Borravaló: {self.borravalo} Fizetés módja : {self.fizetes_modja}"
    
f = open('fuvar.csv', 'rt', encoding='utf-8')
f.readline

taxi = []

for sor in f:
    sor = sor.strip().split(';')
    print(sor)
    taxi.append(Fuvarok(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6]))

print('3.feladat',f"{len(taxi)} fuvar volt")
