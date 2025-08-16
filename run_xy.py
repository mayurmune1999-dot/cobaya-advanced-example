import os, numpy as np, matplotlib
matplotlib.use("Agg")  # save to files (no GUI)
from cobaya import run
import getdist.plots as gdplt

def get_r(x, y): return np.sqrt(x**2 + y**2)
def get_theta(x, y): return np.arctan2(y, x)

info = {
    "likelihood": {"ring": "import_module('my_likelihood').gauss_ring_logp"},
    "params": {
        "x": {"prior": {"min": 0, "max": 2}, "ref": 0.5, "proposal": 0.01},
        "y": {"prior": {"min": 0, "max": 2}, "ref": 0.5, "proposal": 0.01},
        "r": {"derived": get_r},
        "theta": {"derived": get_theta, "latex": r"\\theta", "min": 0, "max": np.pi/2},
    },
    "sampler": {"mcmc": {"Rminus1_stop": 0.001, "max_tries": 1000}},
    "output": "chains/ring_xy",
}

updated_info, sampler = run(info)

os.makedirs("plots", exist_ok=True)
gdsamples = sampler.products(to_getdist=True)["sample"]

gd = gdplt.get_subplot_plotter(width_inch=5)
gd.triangle_plot(gdsamples, ["x", "y"], filled=True)
gd.export("plots/triangle_xy.png")

gd = gdplt.get_subplot_plotter(width_inch=5)
gd.plots_1d(gdsamples, ["r", "theta"], nx=2)
gd.export("plots/oneD_r_theta.png")

print("Saved: plots/triangle_xy.png, plots/oneD_r_theta.png")
