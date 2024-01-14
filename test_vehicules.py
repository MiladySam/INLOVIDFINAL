from unittest import TestCase

from voiture import Voiture

from camion import Camion



class TestVoiture(TestCase):

    def test_tarif_voiture_should_be_15(self):
        self.assertEqual(Voiture('Voiture').tarif(),15)

    def test_tarif_voiture_remorque_should_be_19_5(self):
        voiture = Voiture('Voiture')
        voiture.remorquer()
        self.assertEqual(voiture.tarif(),19.5)




class TestCamion(TestCase):

    def test_tarif_camion_leger_should_be_15(self):
        self.assertEqual(Camion('Camion',4).tarif(),15)


    def test_tarif_camion_moyen_should_be_20(self):
        self.assertEqual(Camion('Camion',5).tarif(),20)

    def test_tarif_camion_lourd_should_be_50(self):
        self.assertEqual(Camion('Camion',11).tarif(),50)

    def test_tarif_longueur_9_moyen_should_be_25(self):

        camion = Camion('Camion',5)
        camion.ajouter_longueur(9)
        self.assertEqual(camion.tarif(), 25)

    def test_tarif_longueur_10_lourd_should_be_60(self):
        camion = Camion('Camion',11)
        camion.ajouter_longueur(10)
        self.assertEqual(camion.tarif(),60)

    def test_remorque_camion(self):
        camion = Camion ('Camion',5)
        camion.remorquer()
        self.assertEqual(camion.tarif(),26)

    def test_remorque_longueur_camion(self):
        camion = Camion('Camion', 3)
        camion.remorquer()
        camion.ajouter_longueur(8)
        self.assertEqual(camion.tarif(), 19.5)

    def test_remorque_longueur20_camion(self):
        camion = Camion('Camion', 11)
        camion.remorquer()
        camion.ajouter_longueur(20)
        self.assertEqual(camion.tarif(), 143)


if __name__ == '__main__':
    TestCase()
