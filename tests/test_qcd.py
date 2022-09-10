import pytest
from natural_units.core import to 
from natural_units.qcd import *

def test_qcd():
	assert qcd_unit(1,{'length':1})*to(meter) == pytest.approx(2.103e-16,rel=1e-3)
	assert qcd_unit(1,{'mass':1})*to(kilogram) == pytest.approx(1.673e-27,rel=1e-3)
	assert qcd_unit(1,{'time':1})*to(second) == pytest.approx(7.015e-25,rel=1e-3)
	assert qcd_unit(1,{'charge':1})*to(coulomb) == pytest.approx(5.291e-19,rel=1e-3)