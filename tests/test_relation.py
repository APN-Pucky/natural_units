import pytest
from natural_units import to
from natural_units.prefix import * 
from natural_units import si,natural, plain_natural


def test_relations():
    for unit in [natural,plain_natural,si]:
        assert unit.hbar*unit.c*to(mega*unit.eV*fempto*unit.meter) == pytest.approx(197.3269804593025)
        assert giga*unit.eV*to(unit.hbar*unit.c*1/(fempto*unit.meter))  == pytest.approx(5.06773075895111)