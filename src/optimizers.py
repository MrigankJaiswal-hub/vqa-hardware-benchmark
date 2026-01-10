import numpy as np
from scipy.optimize import minimize

def classical_optimizer(cost_fn, x0):
    result = minimize(
        cost_fn,
        x0,
        method="COBYLA",
        options={"maxiter": 200}
    )
    return result.x, result.fun
