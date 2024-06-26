class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def ominaisuudet(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def ominaisuudet(self):
        super().ominaisuudet()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def ominaisuudet(self):
        super().ominaisuudet()
        print(f"Päätoimittaja: {self.paatoimittaja}\n")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.ominaisuudet()
hytti_nro_6.ominaisuudet()