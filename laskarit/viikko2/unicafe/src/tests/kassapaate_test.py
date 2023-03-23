import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_setup_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateis_maksu_onnistuu_edullinen_ja_maukas(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riittävä_molemmat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortti_osto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), 'Kortilla on rahaa 7.60 euroa')
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), 'Kortilla on rahaa 3.60 euroa')
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_ei_rahaa(self):
        kortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 0.10 euroa')
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 0.10 euroa')
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(str(self.kortti), 'Kortilla on rahaa 15.00 euroa')
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataus_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -222)
        self.assertEqual(str(self.kortti), 'Kortilla on rahaa 10.00 euroa')
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
