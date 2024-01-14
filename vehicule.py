class Vehicule:

    def __init__(self, name) -> None:
        self.name = name

    def tarif(self) -> float:
        pass

    def __str__(self) -> str:
        return f'le tarif de {self.tarif() if self.tarif() else 0:.2f} CHF pour {self.name} '