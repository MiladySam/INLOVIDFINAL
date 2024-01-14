from vehicule import Vehicule

class Voiture(Vehicule):

    TARIF_BASE = 15

    def __init__(self, name):
        super().__init__(name)
        self.est_remorque = False

    def remorquer(self):
        self.est_remorque = True

    def tarif(self):
        tarif_cal = Voiture.TARIF_BASE

        if self.est_remorque:
            tarif_cal *= 1.3

        return tarif_cal

    def __str__(self) -> str:
        remorque_info = "remorqué" if self.est_remorque else "non remorqué"
        return f'{super().__str__()}{remorque_info}'
