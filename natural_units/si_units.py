from . import base_units as bu

class si_unit(bu.base_unit):
	pass

# base units
meter = metre = si_unit(1, {'metre': 1})
second = si_unit(1, {'second': 1})
kilogram = kg = si_unit(1, {'kilogram': 1})
ampere = si_unit(1, {'ampere': 1})
kelvin = si_unit(1, {'kelvin': 1})
mol = mole = si_unit(1, {'mole': 1})
candela = si_unit(1, {'candela': 1})


# derived units
hertz = Hz = 1 / second
joule = J = kg * meter ** 2 / second ** 2
watt = W = joule / second

# defining constants
delta_nu_cs = 9192631770 / second
c = speed_of_light = 299792458 * meter / second
h = planck = 6.62607015e-34 * joule * second
eV = electron_volt = 1.602176634e-19 * joule
k = boltzmann = 1.380649e-23 * joule / kelvin
NA = avogadro = 6.02214076e23 / mole
Kcd 		= 683 *  candela / watt 

