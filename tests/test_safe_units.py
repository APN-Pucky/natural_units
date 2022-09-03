from natural_units.base_units import IncompatibleUnitsException
import pytest
from natural_units.natural_units import *

def test_must_fail():
	with pytest.raises(IncompatibleUnitsException):
		x = meter + joule
	x = meter + second

