import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def total_flip_result(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, heads=False, tails=False):
    """Returns the total flip(heads || tails)"""
    if heads:
        g_values = [
            df1['1B-CH'].iloc[-1] + df1['2A-CH'].iloc[-1],
            df2['1B-CH'].iloc[-1] + df2['5A-CH'].iloc[-1],
            df3['1B-CH'].iloc[-1] + df3['10A-CH'].iloc[-1],
            df4['5A-CH'].iloc[-1] + df4['5B-CH'].iloc[-1],
            df5['1A-CH'].iloc[-1] + df5['1B-CH'].iloc[-1],
            df6['CH'].iloc[-1],
            df7['5A-CH'].iloc[-1] + df7['10A-CH'].iloc[-1],
            df8['1A-CH'].iloc[-1] + df8['10B-CH'].iloc[-1],
            df9['5B-CH'].iloc[-1] + df9['1B-CH'].iloc[-1] + df9['20B-CH'].iloc[-1],
            df10['5B-CH'].iloc[-1] + df10['10B-CH'].iloc[-1],
            df11['1A-CH'].iloc[-1] + df11['10B-CH'].iloc[-1],
            df12['5B-CH'].iloc[-1] + df12['5A-CH'].iloc[-1],
            df13['1A-CH'].iloc[-1] + df13['10A-CH'].iloc[-1],
            df14['H'].iloc[-1],
            df15['1B-CH'].iloc[-1] + df15['5B-CH'].iloc[-1]
        ]
        return sum(g_values)
        
    if tails:
        g_values = [
            df1['1B-CT'].iloc[-1] + df1['2A-CT'].iloc[-1],
            df2['1B-CT'].iloc[-1] + df2['5A-CT'].iloc[-1],
            df3['1B-CT'].iloc[-1] + df3['10A-CT'].iloc[-1],
            df4['5A-CT'].iloc[-1] + df4['5B-CT'].iloc[-1],
            df5['1A-CT'].iloc[-1] + df5['1B-CT'].iloc[-1],
            df6['CT'].iloc[-1],
            df7['5A-CT'].iloc[-1] + df7['10A-CT'].iloc[-1],
            df8['1A-CT'].iloc[-1] + df8['10B-CT'].iloc[-1],
            df9['5B-CT'].iloc[-1] + df9['1B-CT'].iloc[-1] + df9['20B-CT'].iloc[-1],
            df10['5B-CT'].iloc[-1] + df10['10B-CT'].iloc[-1],
            df11['1A-CT'].iloc[-1] + df11['10B-CT'].iloc[-1],
            df12['5B-CT'].iloc[-1] + df12['5A-CT'].iloc[-1],
            df13['1A-CT'].iloc[-1] + df13['10A-CT'].iloc[-1],
            df14['T'].iloc[-1],
            df15['1B-CT'].iloc[-1] + df15['5B-CT'].iloc[-1]
        ]
        return sum(g_values)
    
    return 0