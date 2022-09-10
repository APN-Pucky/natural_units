import pytest
from natural_units import hep, plain_hep, to
from natural_units.prefix import * 
from natural_units import si


def test_relations():
    for unit in [hep,plain_hep,si]:
        assert unit.h_bar*unit.c*to(mega*unit.eV*fempto*unit.meter) == pytest.approx(197.3269804593025)
        assert giga*unit.eV*to(unit.h_bar*unit.c*1/(fempto*unit.meter))  == pytest.approx(5.06773075895111)