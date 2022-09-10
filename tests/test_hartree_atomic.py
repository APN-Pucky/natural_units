import pytest
from natural_units.core import to 
from natural_units.hartree_atomic import *

def test_hartree_atomic():
	assert hartree_atomic_unit(1,{'length':1})*to(meter) == pytest.approx(5.292e-11,rel=1e-3)
	assert hartree_atomic_unit(1,{'mass':1})*to(kilogram) == pytest.approx(9.109e-31,rel=1e-3)
	assert hartree_atomic_unit(1,{'time':1})*to(second) == pytest.approx(2.419e-17,rel=1e-3)
	assert hartree_atomic_unit(1,{'charge':1})*to(coulomb) == pytest.approx(1.602e-19,rel=1e-3)