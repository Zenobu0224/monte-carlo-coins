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


fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Dashboard", fontsize=15, fontweight="bold")


# PLOT 1 - Stacked bar chart

categories = ['Old Coin', 'New Coin']
x = np.arange(len(categories))
width = 0.35

# Heads bars (left side of each category)
# Old Heads - stacked
axes[0,0].bar(x[0] - width/2, old1_heads, width, label='1 Peso', color='#1f77b4')
axes[0,0].bar(x[0] - width/2, old5_heads, width, bottom=old1_heads, label='5 Peso', color='#ff7f0e')
axes[0,0].bar(x[0] - width/2, old10_heads, width, bottom=old1_heads + old5_heads, label='10 Peso', color='#2ca02c')
axes[0,0].bar(x[0] - width/2, old_others_heads, width, bottom=old1_heads + old5_heads + old10_heads, label='Others', color='#d62728')

# New Heads - stacked
axes[0,0].bar(x[1] - width/2, new1_heads, width, color='#1f77b4')
axes[0,0].bar(x[1] - width/2, new5_heads, width, bottom=new1_heads, color='#ff7f0e')
axes[0,0].bar(x[1] - width/2, new10_heads, width, bottom=new1_heads + new5_heads, color='#2ca02c')
axes[0,0].bar(x[1] - width/2, new_others_heads, width, bottom=new1_heads + new5_heads + new10_heads, color='#d62728')

# Tails bars (right side of each category)
# Old Tails - stacked
axes[0,0].bar(x[0] + width/2, old1_tails, width, color='#1f77b4', alpha=0.6)
axes[0,0].bar(x[0] + width/2, old5_tails, width, bottom=old1_tails, color='#ff7f0e', alpha=0.6)
axes[0,0].bar(x[0] + width/2, old10_tails, width, bottom=old1_tails + old5_tails, color='#2ca02c', alpha=0.6)
axes[0,0].bar(x[0] + width/2, old_others_tails, width, bottom=old1_tails + old5_tails + old10_tails, color='#d62728', alpha=0.6)

# New Tails - stacked
axes[0,0].bar(x[1] + width/2, new1_tails, width, color='#1f77b4', alpha=0.6)
axes[0,0].bar(x[1] + width/2, new5_tails, width, bottom=new1_tails, color='#ff7f0e', alpha=0.6)
axes[0,0].bar(x[1] + width/2, new10_tails, width, bottom=new1_tails + new5_tails, color='#2ca02c', alpha=0.6)
axes[0,0].bar(x[1] + width/2, new_others_tails, width, bottom=new1_tails + new5_tails + new10_tails, color='#d62728', alpha=0.6)

# Customize the plot
axes[0,0].set_xlabel('Coin Type')
axes[0,0].set_ylabel('Count')
axes[0,0].set_title('Coin Flips: Heads vs Tails (Stacked)')
axes[0,0].set_xticks(x)
axes[0,0].set_xticklabels(categories)
axes[0,0].grid(axis='y', alpha=0.3)

# Add custom legend for coin denominations and heads/tails
legend_elements = [
    Patch(facecolor='#1f77b4', label='1 Peso'),
    Patch(facecolor='#ff7f0e', label='5 Peso'),
    Patch(facecolor='#2ca02c', label='10 Peso'),
    Patch(facecolor='#d62728', label='Others')
]
axes[0,0].legend(handles=legend_elements, loc='upper left')



# PLOT 2 - Pie chart

pie_label = ["Overall Heads", "Overall Tails"]
full_heads = total_flip_result(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, heads=True)
full_tails = total_flip_result(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, tails=True)
sizes = [full_heads, full_tails]
explode = (0, 0.1)

axes[0,1].pie(sizes, labels=pie_label, autopct="%1.1f%%", colors=["#35d267", "#d8bef1"], explode=explode, shadow=True, startangle=360)
axes[0,1].legend()
axes[0,1].set_title("Combined H & T", fontweight="bold")



# PLOT 3 - Cumulative line plot (Wood vs Tiles)

# WOODS HEADS
# For df1: columns with -H suffix where 1=heads, so we can use directly
# For others: columns with -H suffix where 1=heads, so we can use directly
heads_wood1 = concat_df(df1['1B'], df2['1B-H'], df3['1B-H'], df5['1A-H'], df5['1B-H'], df8['1A-H'], heads=True)
heads_wood5 = concat_df(df2['5A-H'], df4['5A-H'], df4['5B-H'], df6['5B-H'], df7['5A-H'], heads=True)
heads_wood10 = concat_df(df3['10A-H'], df7['10A-H'], df8['10B-H'], heads=True)
heads_wood_others = concat_df(df1['2A'], df6['20B-H'], heads=True)

# WOODS TAILS
# For df1: columns with -T suffix where 1=tails (but in df1 convention 0=tails, 1=heads)
# So we need to flip df1 columns for tails
# Create flipped versions for df1 tails columns
df1_1B_T_flipped = df1['1B'].replace({0: 1, 1: 0})
df1_2A_T_flipped = df1['2A'].replace({0: 1, 1: 0})

tails_wood1 = concat_df(df1_1B_T_flipped, df2['1B-T'], df3['1B-T'], df5['1A-T'], df5['1B-T'], df8['1A-T'], tails=True)
tails_wood5 = concat_df(df2['5A-T'], df4['5A-T'], df4['5B-T'], df6['5B-T'], df7['5A-T'], tails=True)
tails_wood10 = concat_df(df3['10A-T'], df7['10A-T'], df8['10B-T'], tails=True)
tails_wood_others = concat_df(df1_2A_T_flipped, df6['20B-T'], tails=True)

# TILES HEADS
heads_tiles1 = concat_df(df9['1B-H'], df11['1A-H'], df13['1A-H'], df14['1A-H'], df15['1B-H'], heads=True)
heads_tiles5 = concat_df(df9['5B-H'], df10['5B-H'], df12['5B-H'], df12['5A-H'], df15['5B-H'], heads=True)
heads_tiles10 = concat_df(df10['10B-H'], df11['10B-H'], df13['10A-H'], heads=True)
heads_tiles_others = concat_df(df9['20B-H'], df14['20B-H'], heads=True)

# TILES TAILS
tails_tiles1 = concat_df(df9['1B-T'], df11['1A-T'], df13['1A-T'], df14['1A-T'], df15['1B-T'], tails=True)
tails_tiles5 = concat_df(df9['5B-T'], df10['5B-T'], df12['5B-T'], df12['5A-T'], df15['5B-T'], tails=True)
tails_tiles10 = concat_df(df10['10B-T'], df11['10B-T'], df13['10A-T'], tails=True)
tails_tiles_others = concat_df(df9['20B-T'], df14['20B-T'], tails=True)

# Get final values for comparison
wood_heads_final = [heads_wood1.iloc[-1], heads_wood5.iloc[-1], heads_wood10.iloc[-1], heads_wood_others.iloc[-1]]
wood_tails_final = [tails_wood1.iloc[-1], tails_wood5.iloc[-1], tails_wood10.iloc[-1], tails_wood_others.iloc[-1]]
tiles_heads_final = [heads_tiles1.iloc[-1], heads_tiles5.iloc[-1], heads_tiles10.iloc[-1], heads_tiles_others.iloc[-1]]
tiles_tails_final = [tails_tiles1.iloc[-1], tails_tiles5.iloc[-1], tails_tiles10.iloc[-1], tails_tiles_others.iloc[-1]]

# Create comparison bar chart
y_labels = ["1 Peso", "5 Peso", "10 Peso", "Others"]
y_pos = np.arange(len(y_labels))
bar_height = 0.2

# Wood Heads
axes[1,0].barh(y_pos - 1.5*bar_height, wood_heads_final, bar_height, label='Wood Heads', color='#1f77b4')
# Wood Tails
axes[1,0].barh(y_pos - 0.5*bar_height, wood_tails_final, bar_height, label='Wood Tails', color='#1f77b4', alpha=0.5)
# Tiles Heads
axes[1,0].barh(y_pos + 0.5*bar_height, tiles_heads_final, bar_height, label='Tiles Heads', color='#ff7f0e')
# Tiles Tails
axes[1,0].barh(y_pos + 1.5*bar_height, tiles_tails_final, bar_height, label='Tiles Tails', color='#ff7f0e', alpha=0.5)

axes[1,0].set_yticks(y_pos)
axes[1,0].set_yticklabels(y_labels)
axes[1,0].set_xlabel('Count')
axes[1,0].set_title('Wood vs Tiles Comparison by Denomination')
axes[1,0].grid(True, alpha=0.3, axis='x')
axes[1,0].legend(loc='best')



# PLOT 4 - Cumulative trends over time

# Plot cumulative trends for wood coins
axes[1,1].plot(range(len(heads_wood1)), heads_wood1, label='Wood 1P (H)', color='#1f77b4', linewidth=2)
axes[1,1].plot(range(len(heads_wood5)), heads_wood5, label='Wood 5P (H)', color='#ff7f0e', linewidth=2)
axes[1,1].plot(range(len(heads_wood10)), heads_wood10, label='Wood 10P (H)', color='#2ca02c', linewidth=2)
axes[1,1].plot(range(len(heads_tiles1)), heads_tiles1, label='Tiles 1P (H)', color='#1f77b4', linestyle='--', linewidth=2)
axes[1,1].plot(range(len(heads_tiles5)), heads_tiles5, label='Tiles 5P (H)', color='#ff7f0e', linestyle='--', linewidth=2)
axes[1,1].plot(range(len(heads_tiles10)), heads_tiles10, label='Tiles 10P (H)', color='#2ca02c', linestyle='--', linewidth=2)

axes[1,1].set_xlabel('Flip Number')
axes[1,1].set_ylabel('Cumulative Heads Count')
axes[1,1].set_title('Cumulative Heads Over Time')
axes[1,1].grid(True, alpha=0.3)
axes[1,1].legend(loc='best', fontsize=8)

plt.tight_layout()
plt.show()