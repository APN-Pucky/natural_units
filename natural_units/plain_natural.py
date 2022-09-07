from . import natural as su

# Here we just mirror natural, but without mass dimensions
for k in su.__dir__():
    v = su.__getattribute__(k)
    if isinstance(v, su.natural_unit):
        globals()[k] = v.value
    elif isinstance(v, float):
        globals()[k] = v
    elif isinstance(v, int):
        globals()[k] = v