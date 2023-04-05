import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import uniform


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    z_alpha = uniform.ppf(alpha, loc=0.047, scale=b-0.047)
    b = np.max(x)
    se = np.sqrt(b*(1-b)/n)
    z_se = se * uniform.ppf(1-alpha/2, loc=0, scale=1)
    left = max(0.047, b - z_se)
    right = min(1, b - z_alpha)
    return (left, right)



