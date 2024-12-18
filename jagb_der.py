import numpy as np
"""
Returns smoothed dm/dr and r
"""

def derivative(JAGB_modes, mean_gc_radius):
    
    
    int_ = int(np.ceil(len(JAGB_modes)/ 6)) # smooth derivative
    
    return (JAGB_modes[int_:] - JAGB_modes[:-int_])/(mean_gc_radius[int_:] - mean_gc_radius[:-int_]), (mean_gc_radius[int_:] - mean_gc_radius[:-int_]) /2 + mean_gc_radius[:-int_]
