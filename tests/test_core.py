import pytest
from natural_units import *
from natural_units import hartree_atomic as ha
from natural_units import particle_atomic as pa
from natural_units import planck 
from natural_units import qcd
from natural_units import stoney
from natural_units import si

def test_conversions():
	assert convert(meter, centi*meter) == pytest.approx(100)
	assert kilo*gram*to(gram) == pytest.approx(1000)
	assert gram * to(kilo*gram) == pytest.approx(0.001)
	
def test_to_si():
	assert ha.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)
	assert pa.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)
	assert pa.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)
	assert planck.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)
	assert qcd.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)
	assert stoney.meter.to_si()*to(si.meter) == pytest.approx(1.0,rel=1e-3)

def test_from_si():
	assert ha.hartree_atomic_unit.from_si(si.meter)*to(ha.meter) == pytest.approx(1.0,rel=1e-3)
	assert pa.particle_atomic_unit.from_si(si.meter)*to(pa.meter) == pytest.approx(1.0,rel=1e-3)
	assert qcd.qcd_unit.from_si(si.meter)*to(qcd.meter) == pytest.approx(1.0,rel=1e-3)
	assert stoney.stoney_unit.from_si(si.meter)*to(stoney.meter) == pytest.approx(1.0,rel=1e-3)
	assert planck.planck_unit.from_si(si.meter)*to(planck.meter) == pytest.approx(1.0,rel=1e-3)