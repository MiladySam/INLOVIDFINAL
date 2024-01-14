En tant qu'usager souhaitant traverser le tunnel du Gothard avec mon véhicule, je souhaite utiliser un outil de calcul de prix de billet pour connaître le coût exact de ma traversée. L'outil doit prendre en compte les différentes catégories de véhicules définies par les Chemins de fer fédéraux suisses (CFF) et appliquer les règles de tarification suivantes.


1. Identification de la catégorie du véhicule :

cat 1. Si le véhicule est une voiture, le tarif est fixé à 15 CHF.
cat 2. Si le véhicule est un camion sans remorque et pèse moins de 4 tonnes, le tarif est également de 15 CHF.
cat 3. Si le véhicule est un camion avec remorque, les règles spécifiques s'appliquent, et un supplément de 30% est ajouté au prix final.


2. Calcul du tarif pour les camions de 4 tonnes et plus :
Si le poids du camion est inférieur à 10 tonnes, le tarif est de 20 CHF.
Si le poids du camion est supérieur à 10 tonnes, le tarif est de 50 CHF.


3. Calcul du tarif en fonction de la longueur pour les camions de 4 tonnes et plus :
Si la longueur du camion est supérieure à 8 mètres, une taxe de 5 CHF est perçue par mètre supplémentaire.


4. Calcul du prix final pour les camions de 4 tonnes et plus :
Si la longueur du camion est supérieure à 8 mètres, la taxe de longueur est ajoutée au tarif calculé.
Le supplément de 30% est ajouté pour les camions avec remorque quels que soient leur poids et leur longueur.


5. Récapitulatif du prix final :
Le prix final est obtenu en additionnant le tarif de base, la taxe de longueur (si applicable), et le supplément pour les camions avec remorque.














 self.poids = poids
        self.longueur = 0  # Initialiser la longueur à 0
        self.remorque = False

    def ajouter_longueur(self, longueur: float) -> None:
        self.longueur = longueur

    def ajouter_remorque(self) -> None:
        self.remorque = True

    def tarif(self) -> float:
        # Tarif de base selon le poids
        if self.poids <= 4:
            tarif_base = 15
        elif 4 <= self.poids < 10:
            tarif_base = 20
        elif self.poids >= 10:
            tarif_base = 50
        if self.longueur > 8:
            tarif_base += 5 * (self.longueur - 8)

        # Ajouter la taxe de remorque
        if self.remorque:
            tarif_base *= 1.3

        return tarif_base

    # from voiture import Voiture
    # from camion import Camion
    #
    # class TestVoiture(TestCase):
    #
    #     def test_tarif_voiture_should_be_15(self):
    #         self.assertEqual(Voiture('voiture').tarif(), 15)
    #
    # class TestCamion(TestCase):
    #
    #     def test_tarif_camion_under_4ton_should_be_15(self):
    #         self.assertEqual(Camion(3, 'Camion').tarif(), 15)
    #
    #     def test_tarif_camion_greater_than_4ton_should_be_20(self):
    #         self.assertEqual(Camion(5, 'Camion').tarif(), 20)
    #
    #     def test_tarif_camion_greater_than_10ton_should_be_50(self):
    #         self.assertEqual(Camion(11, 'Camion').tarif(), 50)
    #
    #     def test_tarif_camion_longueur_sup_8_et_greater_4ton(self):
    #         camion = Camion(5, 'Camion')
    #         camion.ajouter_longueur(8)
    #         self.assertEqual(camion.tarif(), 20)
    #
    #     def test_camion_with_remorque(self):
    #         camion = Camion(5, 'Camion')
    #         camion.ajouter_remorque()
    #         self.assertEqual(camion.tarif(), 26)