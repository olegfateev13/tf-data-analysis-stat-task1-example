import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.stats import lognorm

chat_id = 263008738 # Ваш chat ID, не меняйте название переменной
def log_likelihood(a, x):
    return -np.sum(lognorm.logpdf(x, s=a))
def solution(x: np.array) -> float:
    result = minimize(log_likelihood, 1, args=(x,))
    return result.x[0] # Ваш ответ
