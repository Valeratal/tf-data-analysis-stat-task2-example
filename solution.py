import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной

def proportion_confidence_interval(p: float, n: int, alpha: float = 0.05) -> tuple:
    """
    Calculate the confidence interval for a population proportion.

    Parameters:
    p (float): the proportion of successes in the sample
    n (int): the sample size
    alpha (float): the level of significance (default is 0.05)

    Returns:
    tuple: a tuple containing the lower and upper bounds of the confidence interval
    """
    z = norm.ppf(1 - alpha / 2)
    phat = p
    se = np.sqrt(p * (1 - p) / n)
    lower = phat - z * se
    upper = phat + z * se
    return (lower, upper)
