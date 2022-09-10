import pytest
from natural_units.core import to 
from natural_units.planck import *

def test_planck():
	assert planck_unit(1,{'length':1})*to(meter) == pytest.approx(1.616e-35,rel=1e-2)
	assert planck_unit(1,{'mass':1})*to(kilogram) == pytest.approx(2.176e-8,rel=1e-2)
	assert planck_unit(1,{'time':1})*to(second) == pytest.approx(5.391e-44,rel=1e-2)
	assert planck_unit(1,{'temperature':1})*to(kelvin) == pytest.approx(1.417e32,rel=1e-2)