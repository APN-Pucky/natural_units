"""https://en.wikipedia.org/wiki/Planck_units"""

import math
import scipy.constants as const
from .prefix import *
from . import base as bu
pi = math.pi

class planck_unit(bu.base_unit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)


speed_of_light = c = planck_unit(1,{'length':1,'time':-1})
reduced_planck_constant= h_bar = planck_unit(1,{'mass':1,'length':2,'time':-1})
planck_constant = h = 2*pi*h_bar
gravitational_constant = G = planck_unit(1,{'mass':-1,'length':3,'time':-2})
boltzmann_constant = k_B = planck_unit(1,{'mass':1,'length':2,'time':-2,'temperature':-1})

# measured
gravitational_coupling_constant = alpha_G = const.G*const.m_e**2/const.hbar/const.c
proton_to_electron_mass_ratio = const.proton_mass/const.electron_mass


mass_eletron = m_e = (h_bar*c*gravitational_coupling_constant/G)**(1/2)
mass_proton = m_p = proton_to_electron_mass_ratio*m_e

# undefined
fine_structure_constant = alpha = None
elementary_charge = e = None
vacuum_permittivity = epsilon_0 = None
coulomb_constant = k_e = None
