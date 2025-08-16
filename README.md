# Cobaya Advanced Example

This repository contains an advanced example of using [Cobaya](https://cobaya.readthedocs.io/en/latest/) for Bayesian inference in cosmology and statistics.  
It includes custom likelihoods and run scripts to demonstrate how to extend Cobaya for research use.

## Repository Structure

- **`my_likelihood.py`** → Custom likelihood definition.  
- **`run_rtheta.py`** → Run script exploring the parameter `r_theta`.  
- **`run_xy.py`** → Run script with two parameters `x` and `y`.  
- **`run_xy_yecy.py`** → Run script with a modified likelihood for `x`, `y`, and extra parameters.  
- **`.gitignore`** → Tells Git which files to ignore (e.g., cache, large outputs).  

## Requirements

- Python 3.9+  
- [Cobaya](https://cobaya.readthedocs.io/en/latest/installation.html)  
- `numpy`, `matplotlib`  

Install dependencies:
```bash
pip install cobaya numpy matplotlib
Running the examples

From inside the repository folder:

# Example run
python run_xy.py

# Another example
python run_rtheta.py


The scripts will run Cobaya and produce MCMC chains and plots.

Output

Chains are saved in the chains/ directory.

Plots (e.g., triangle plots of posteriors) are saved as .png files.

Example plot:

<!-- (Add this later when you save a plot) -->

Next Steps

Extend the likelihood to cosmological datasets.

Add YAML equivalents of the run scripts.

Document results in a docs/ folder.
