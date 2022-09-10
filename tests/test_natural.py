import pytest
from natural_units.core import to 
from natural_units.hep import *

def test_massdimensions_value():
	assert eV.units["massdimension"] == 1

def test_massdimension_type():
	meter.check(natural_unit(massdim='length'))
	s.check(natural_unit(massdim='time'))
	gram.check(natural_unit(massdim='mass'))
	kelvin.check(natural_unit(massdim='temperature'))
	barn.check(natural_unit(massdim='length')**2)
	u.check(natural_unit(massdim='mass'))

def test_planck():
	assert planck_length * to(centi*meter) == pytest.approx(1.6e-33,rel=1e-2)
	assert planck_time * to(second) == pytest.approx(5.4e-44,rel=1e-2)
	assert planck_temperature * to(kelvin) == pytest.approx(1.4e32,rel=1e-2)