import pytest
from natural_units.prefix import * 
from natural_units import si,natural, plain_natural


def test_relations():
    for unit in [si,natural,plain_natural]:
        assert unit.hbar*unit.c/(mega*unit.eV*fempto*unit.meter) == pytest.approx(197.3269804593025)