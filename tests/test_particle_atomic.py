import pytest
from natural_units.core import to 
from natural_units.particle_atomic import *

def test_particle_atomic():
	assert particle_atomic_unit(1,{'length':1})*to(meter) == pytest.approx(3.862e-13,rel=1e-3)
	assert particle_atomic_unit(1,{'mass':1})*to(kilogram) == pytest.approx(9.109e-31,rel=1e-3)
	assert particle_atomic_unit(1,{'time':1})*to(second) == pytest.approx(1.288e-21,rel=1e-3)
	assert particle_atomic_unit(1,{'charge':1})*to(coulomb) == pytest.approx(5.291e-19,rel=1e-3)