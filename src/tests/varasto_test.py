import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, alku_saldo = 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_jos_uudella_varastolla_negatiivinen_saldo(self):
        self.varasto = Varasto(10, alku_saldo = -5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_jos_uudella_varastolla_sama_saldo_ja_tilavuus(self):
        self.varasto = Varasto(10, alku_saldo = 10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        # varasto antaa vain niin paljon kuinka siellä on
        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        # varastoon voi lisätä vain sen tilavuuden verran eli 10

        self.assertAlmostEqual(self.varasto.saldo, 10)


    def test_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_tilavuus_ei_voi_olla_negatiivinen(self):
        self.varasto = Varasto(-10)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_tulostaa_oikean_outputin(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 8, vielä tilaa 2")

