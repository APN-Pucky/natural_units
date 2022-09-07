import pytest
from natural_units.prefix import kilo
from natural_units import geometrized as gu
from natural_units.core import to

def test_geometrized():
    assert gu.s*to(gu.cm) == pytest.approx(2.9979e10,rel=1e-4)
    assert gu.g*gu.cm**-3 * to(gu.cm**-2) == pytest.approx(7.4261e-29)
    assert gu.M0*to(kilo*gu.gram) == pytest.approx(1.9884e30 )