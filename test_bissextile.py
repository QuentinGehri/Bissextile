from bissextile import Bissextile
import unittest
import random

class TestBissextile(unittest.TestCase):

    def creer_liste_bissextile(self):
        liste = []
        for i in range(1900,3001,4):
            liste.append(i)
        return liste

    def creer_liste_pas_bissextile(self):
        liste = []
        for i in range(1901,3000):
            if (Bissextile().est_bissextile(i) == False) :
                liste.append(i)
        return liste

    def test_non_divise_par_4_false(self):
        self.assertEqual(False, Bissextile().est_bissextile(1999))

    def test_divise_par_4_true(self):
        self.assertEqual(True, Bissextile().est_bissextile(1996))

    def test_divise_par_100_true(self):
        self.assertEqual(True,  Bissextile().est_bissextile(2000))

    def test_non_divise_par_100_false(self):
        self.assertEqual(False, Bissextile().est_bissextile(2100))

    def test_affichage_bissextile(self):
        liste = TestBissextile.creer_liste_bissextile(self)
        random_num = random.choice(liste)
        self.assertEqual('l\'année est bissextile', Bissextile().affiche_result(random_num))

    def test_affichage_pas_bissextile(self):
        liste = TestBissextile.creer_liste_pas_bissextile(self)
        random_num = random.choice(liste)
        self.assertEqual('l\'année est pas bissextile', Bissextile().affiche_result(random_num))




if __name__ == '__main__':
    unittest.main()  # pragma: no cover
