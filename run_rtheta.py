# run_rtheta.py
from cobaya.run import run
import getdist.plots as gd
import matplotlib.pyplot as plt

info = {
    "params": {
        "r": {"prior": {"min": 0, "max": 2}, "latex": "r"},
        "theta": {"prior": {"min": 0, "max": 6.283"}, "latex": r"\theta"},
        "x": {"derived": "r*cos(theta)", "latex": "x"},
        "y": {"derived": "r*sin(theta)", "latex": "y"},
    },
    "likelihood": {"my_likelihood.my_likelihood": None},
    "sampler": {"mcmc": {"max_samples": 10000}},
}

updated_info, products = run(info)

# Plotting with GetDist
samples = products["sample"]
g = gd.get_subplot_plotter()
g.triangle_plot(samples, ["r", "theta", "x", "y"], filled=True)

plt.savefig("plots/triangle_rtheta.png")
plt.show()
