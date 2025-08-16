import numpy as np
from scipy import stats

def gauss_ring_logp(x, y, mean_radius=1.0, std=0.02):
    """Gaussian ring likelihood centered at 0 with radius=1."""
    r = np.sqrt(x**2 + y**2)
    return stats.norm.logpdf(r, loc=mean_radius, scale=std)

def gauss_ring_logp_with_derived(x, y, mean_radius=1.0, std=0.02):
    """Return (logp, derived) so Cobaya can record r and theta from inside."""
    r = np.sqrt(x**2 + y**2)
    derived = {"r": r, "theta": np.arctan2(y, x)}
    return stats.norm.logpdf(r, loc=mean_radius, scale=std), derived
