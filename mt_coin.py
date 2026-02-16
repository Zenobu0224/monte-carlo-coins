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


def result_per_coin(*dfs):
    """Sum any number of coin flip results"""
    return sum(dfs)


def concat_df(*series, heads=False, tails=False):
    """Concatenate multiple series and return cumulative sum
    
    For normal convention columns (most dataframes):
        - H columns: 1=heads, 0=tails -> count 1s for heads
        - T columns: 1=tails, 0=heads -> count 1s for tails
    
    For df1 with reversed convention:
        - Raw columns have 1=heads, 0=tails
        - But when passed to this function, they should already be in correct format
    """
    if heads or tails:
        # Combine all series into one
        combined = pd.concat(list(series), ignore_index=True)
        
        # Return cumulative sum (assuming all series are already in correct format)
        return np.cumsum(combined)
    
    return np.array([0])


# DATAFRAMES (G1 - G15)
df1 = pd.read_csv("g1.csv")
df2 = pd.read_csv("g2.csv")
df3 = pd.read_csv("g3.csv")
df4 = pd.read_csv("g4.csv")
df5 = pd.read_csv("g5.csv")
df6 = pd.read_csv("g6.csv")
df7 = pd.read_csv("g7.csv")
df8 = pd.read_csv("g8.csv")
df9 = pd.read_csv("g9.csv")
df10 = pd.read_csv("g10.csv")
df11 = pd.read_csv("g11.csv")
df12 = pd.read_csv("g12.csv")
df13 = pd.read_csv("g13.csv")
df14 = pd.read_csv("g14.csv")
df15 = pd.read_csv("g15.csv")


# var for old
old1_heads_df14_cumsum = np.cumsum(df14['1A-H'])
old1_heads_df14 = old1_heads_df14_cumsum.iloc[-1]
old1_tails_df14_cumsum = np.cumsum(df14['1A-T'])
old1_tails_df14 = old1_tails_df14_cumsum.iloc[-1]

old1_heads = result_per_coin(df5['1A-CH'].iloc[-1], df8['1A-CH'].iloc[-1], df11['1A-CH'].iloc[-1], df13['1A-CH'].iloc[-1], old1_heads_df14)
old5_heads = result_per_coin(df2['5A-CH'].iloc[-1], df4['5A-CH'].iloc[-1], df7['5A-CH'].iloc[-1], df12['5A-CH'].iloc[-1])
old10_heads = result_per_coin(df3['10A-CH'].iloc[-1], df7['10A-CH'].iloc[-1], df13['10A-CH'].iloc[-1])
old_others_heads = result_per_coin(df1['2A-CH'].iloc[-1])

old1_tails = result_per_coin(df5['1A-CT'].iloc[-1], df8['1A-CT'].iloc[-1],  df11['1A-CT'].iloc[-1], df13['1A-CT'].iloc[-1], old1_tails_df14)
old5_tails = result_per_coin(df2['5A-CT'].iloc[-1], df4['5A-CT'].iloc[-1], df7['5A-CT'].iloc[-1], df12['5A-CT'].iloc[-1])
old10_tails = result_per_coin(df3['10A-CT'].iloc[-1], df7['10A-CT'].iloc[-1], df13['10A-CT'].iloc[-1])
old_others_tails = result_per_coin(df1['2A-CT'].iloc[-1])


# var for new
new5_heads_df6 = df6['5B-CH'].iloc[-1]
new5_tails_df6 = df6['5B-CT'].iloc[-1]
others1_heads_df6 = df6['20B-CH'].iloc[-1]
others1_tails_df6 = df6['20B-CT'].iloc[-1]

others2_heads_df14_cumsum = np.cumsum(df14['20B-H'])
others2_heads_df14 = others2_heads_df14_cumsum.iloc[-1]
others2_tails_df14_cumsum = np.cumsum(df14['20B-T'])
others2_tails_df14 = others2_tails_df14_cumsum.iloc[-1]

new1_heads = result_per_coin(df1['1B-CH'].iloc[-1], df2['1B-CH'].iloc[-1], df3['1B-CH'].iloc[-1], df5['1B-CH'].iloc[-1], df9['1B-CH'].iloc[-1], df15['1B-CH'].iloc[-1])
new5_heads = result_per_coin(new5_heads_df6, df4['5B-CH'].iloc[-1], df9['5B-CH'].iloc[-1], df10['5B-CH'].iloc[-1], df12['5B-CH'].iloc[-1], df15['5B-CH'].iloc[-1])
new10_heads = result_per_coin(df8['10B-CH'].iloc[-1], df10['10B-CH'].iloc[-1], df11['10B-CH'].iloc[-1])
new_others_heads = result_per_coin(others1_heads_df6, df9['20B-CH'].iloc[-1])

new1_tails = result_per_coin(df1['1B-CT'].iloc[-1], df2['1B-CT'].iloc[-1], df3['1B-CT'].iloc[-1], df5['1B-CT'].iloc[-1], df9['1B-CT'].iloc[-1], df15['1B-CT'].iloc[-1])
new5_tails = result_per_coin(new5_tails_df6, df4['5B-CT'].iloc[-1], df9['5B-CT'].iloc[-1], df12['5B-CT'].iloc[-1], df15['5B-CT'].iloc[-1], df10['5B-CT'].iloc[-1])
new10_tails = result_per_coin(df8['10B-CT'].iloc[-1], df10['10B-CT'].iloc[-1], df11['10B-CT'].iloc[-1])
new_others_tails = result_per_coin(others1_tails_df6, df9['20B-CT'].iloc[-1])