from vehicule import Vehicule

class Camion(Vehicule):
    def __init__(self, name, poids):
        super().__init__(name)
        self.poids = poids
        self.longueur = 0
        self.remorque = False

    def ajouter_longueur(self, longueur):
        self.longueur = longueur

    def remorquer(self):
        self.remorque = True

    def tarif(self):
        tarif_base = 0

        if self.poids <= 4:
            tarif_base = 15
        elif 4 <= self.poids < 10:
            tarif_base = 20
        elif self.poids > 10:
            tarif_base = 50

        if self.longueur > 8:
            tarif_base += 5 * (self.longueur - 8)

        if self.remorque:
            tarif_base *= 1.3

        return tarif_base

    def __str__(self) -> str:
        remorque_info = "remorqué" if self.remorque else "non remorqué"
        return f'{super().__str__()} avec un poids de {self.poids} tonnes et une longueur de {self.longueur}, qui est {remorque_info}'


