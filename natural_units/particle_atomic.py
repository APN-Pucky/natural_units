"""https://en.wikipedia.org/wiki/Natural_units"""
import math
import scipy.constants as const
from .prefix import kilo
from . import base as bu
pi = math.pi

class particle_atomic_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)


speed_of_light = c = particle_atomic_unit(1,{'length':1,'time':-1})
electron_mass = m_e = particle_atomic_unit(1,{'mass':1})
reduced_planck_constant= h_bar = particle_atomic_unit(1,{'mass':1,'length':2,'time':-1})
planck_constant = h = 2*pi*h_bar
vacuum_permittivity = epsilon_0 = particle_atomic_unit(1,{'mass':-1,'length':-3,'time':2,'charge':2}) 

# measured
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass
fine_structure_constant = alpha = const.fine_structure
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c

# derived
elementary_charge = e = (4*pi*alpha* epsilon_0 * h_bar * c) **(1/2)
coloumb_constant = k_e = 1/(4*pi*epsilon_0)
gravitational_constant = G = alpha_G * h_bar*c /m_e**2
proton_mass = m_p = m_e*proton_to_electron_mass_ratio

# undefined
boltzmann_constant = k_B = None

# si conversion
meter = metre = 1/(const.hbar/(const.m_e*const.c)) * particle_atomic_unit(1,{'length':1})
gram = 1/kilo * 1/m_e * particle_atomic_unit(1,{'mass':1})
kilogram = kilo*gram
second = 1/(const.hbar/const.m_e/const.c**2) * particle_atomic_unit(1,{'time':1})
coulomb = 1/(const.epsilon_0*const.hbar*const.c)**(1/2) * particle_atomic_unit(1,{'charge':1})
ampere = coulomb/second