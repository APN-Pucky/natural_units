import natural_units.si as si
import natural_units.plain_natural as u
import natural_units.natural as nu

def test_si():
	assert str(si.meter) == "1 m"
	assert str(u.meter) == "5067730.758951109"
	assert str(nu.meter) == "5067730.758951109[-1]"
