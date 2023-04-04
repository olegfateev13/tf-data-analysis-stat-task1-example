import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.stats import lognorm

chat_id = 263008738 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x -= 331
    result = np.mean(np.log(x))
    return result # Ваш ответ
