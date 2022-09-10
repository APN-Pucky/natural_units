import pytest
from natural_units.core import to 
from natural_units.stoney import *

def test_stoney():
	assert stoney_unit(1,{'length':1})*to(meter) == pytest.approx(1.38068e-36,rel=1e-3)
	assert stoney_unit(1,{'mass':1})*to(kilogram) == pytest.approx(1.85921e-9,rel=1e-3)
	assert stoney_unit(1,{'time':1})*to(second) == pytest.approx(4.60544e-45,rel=1e-3)
	assert stoney_unit(1,{'charge':1})*to(coulomb) == pytest.approx(1.60218e-19,rel=1e-3)