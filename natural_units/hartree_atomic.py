"""https://en.wikipedia.org/wiki/Hartree_atomic_units"""
import math
from turtle import speed
import scipy.constants as const
from .prefix import *
from . import base as bu
pi = math.pi

class hartree_atomic_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

electron_charge = e = hartree_atomic_unit(1,{'charge':1})
electron_mass = m_e = hartree_atomic_unit(1,{'mass':1})
reduced_planck_constant= h_bar = hartree_atomic_unit(1,{'mass':1,'length':2,'time':-1})
coulomb_constant = k_e = hartree_atomic_unit(1,{'mass':-1,'length':-3,'time':4,'charge':2})

# measured
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass
fine_structure_constant = alpha = const.fine_structure
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c

vacuum_permittivity = epsilon_0 = 1/(4*pi*k_e)
speed_of_light = c = e**2/(4*pi*epsilon_0*alpha*h_bar)
gravitational_constant = G = alpha_G * h_bar*c /m_e**2
proton_mass = m_p = m_e*proton_to_electron_mass_ratio

# undefined
boltzmann_constant = k_B = None

meter = metre = 1/(4*pi*const.epsilon_0*const.hbar**2/(const.m_e**2*const.e**2)) * hartree_atomic_unit(1,{'length':1})
gram = 1/kilo * 1/m_e * hartree_atomic_unit(1,{'mass':1})
second = 1/((4*pi*const.epsilon_0)**2*const.hbar**3/(const.m_e*const.e**4)) * hartree_atomic_unit(1,{'time':1})
coulomb = 1/const.e * hartree_atomic_unit(1,{'charge':1})
ampere = coulomb/second