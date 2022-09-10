from natural_units.base import IncompatibleUnitsException
import pytest
from natural_units import hep as nu
from natural_units import si as si

def test_must_fail():
	with pytest.raises(IncompatibleUnitsException):
		x = si.meter + si.second
	with pytest.raises(IncompatibleUnitsException):
		x = nu.meter + nu.joule
	x = nu.meter + nu.second

