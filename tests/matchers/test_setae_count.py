"""Test setae count trait matcher."""

import unittest

from src.pylib.pipeline import PIPELINE
from traiter.pylib.util import shorten

NLP = PIPELINE.trait_list


class TestRSetaeCount(unittest.TestCase):
    """Test range trait matcher."""

    def test_setae_count_01(self):
        self.assertEqual(
            NLP(shorten("""
                 One long Dorsal Principal Head Seta (DPHS),
                 one small Dorsal Accessory Head Seta (DAcHS)
                 anteromedial to DPHS,
                 one Dorsal Posterior Central Head Seta (DPoCHS),
                 two to three Dorsal Preantennal Head Setae (DPaHS),
                 two Sutural Head Setae (SHS),
                 three Dorsal Marginal Head Setae (DMHS),
                 three to four Apical Head Setae (ApHS),
                 and one fairly large Ventral Preantennal Head Seta (VPaHS).
                 """)),
            [{'count': 1, 'setae': 'dorsal principal head setae',
              'trait': 'setae_count', 'start': 0, 'end': 42},
             {'count': 1, 'setae': 'dorsal accessory head setae',
              'trait': 'setae_count', 'start': 44, 'end': 88},
             {'count': 1, 'setae': 'dorsal posterior central head setae',
              'trait': 'setae_count', 'start': 111, 'end': 158},
             {'low': 2, 'high': 3, 'setae': 'dorsal preantennal head setae',
              'trait': 'setae_count', 'start': 160, 'end': 210},
             {'count': 2, 'setae': 'sutural head setae',
              'trait': 'setae_count', 'start': 212, 'end': 240},
             {'count': 3, 'setae': 'dorsal marginal head setae',
              'trait': 'setae_count', 'start': 242, 'end': 281},
             {'low': 3, 'high': 4, 'setae': 'apical head setae',
              'trait': 'setae_count', 'start': 283, 'end': 321},
             {'count': 1, 'setae': 'ventral preantennal head setae',
              'trait': 'setae_count', 'start': 327, 'end': 381}]
        )

    def test_setae_count_02(self):
        self.assertEqual(
            NLP(shorten(""" no Dorsal Mesothoracic Setae (DMsS); """)),
            [{'count': 0, 'setae': 'dorsal mesothoracic setae',
              'trait': 'setae_count', 'start': 0, 'end': 35}]
        )