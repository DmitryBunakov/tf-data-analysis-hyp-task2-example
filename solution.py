import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import anderson_ksamp

chat_id = 378114682 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    anderson_ksamp([x, y]).pvalue <= 0.03
