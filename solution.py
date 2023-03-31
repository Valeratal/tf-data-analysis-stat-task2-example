import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    lower_bound = np.min(x)
    upper_bound = np.max(x)
    loc = (lower_bound + upper_bound) / 2
    scale = (upper_bound - lower_bound) / np.sqrt(12) # standard deviation of uniform distribution is sqrt((b-a)^2/12)
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc + scale * norm.ppf(1 - alpha / 2)
