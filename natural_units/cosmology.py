import math
from .prefix import *
from . import massdimension as bu

class natural_unit(bu.massdimension_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

pi = math.pi

eV = natural_unit(massdim='energy')
c = natural_unit(massdim='length')/natural_unit(massdim='time')
kb = natural_unit(massdim='energy')/natural_unit(massdim='temperature')
h_bar = natural_unit(massdim='energy')*natural_unit(massdim='time')


# fundamental
_c0 = 299792458 * c  # m/s
_h_bar0 = 4.135667662e-15/(2*pi)*h_bar
_kb0 = 8.617333262145e-5*kb

# from wikipedia https://de.wikipedia.org/wiki/Nat%C3%BCrliche_Einheiten
J = joule = 1/(1.60218e-19)*eV

meter = 1/_h_bar0/_c0 * natural_unit(massdim='length')

s = second = 1/_h_bar0*natural_unit(massdim='time')

gram = 1/kilo*(1/1.78266e-36) * natural_unit(massdim='mass')

# *c0*c0
kelvin = 1*_kb0*natural_unit(massdim='temperature')

# composite
barn = 1e-28*meter**2

u = 1/(6.022141e26)*kilo*gram

Bq = 1/s
Ci = 37*giga * Bq
year = 31556952 * s  # inclusive
Hz = hertz = 1/s
W = watt = J/s

ly = year * c

planck_mass = 1.2e19*giga*eV
planck_length = 1/planck_mass
planck_time = planck_length
planck_temperature = planck_mass
planck_energy = planck_mass