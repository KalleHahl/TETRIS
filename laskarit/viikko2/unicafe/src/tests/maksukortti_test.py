import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 12.00 euroa')

    def test_saldo_vahenee_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 8.00 euroa')
    
    def test_saldo_ei_muutu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')
