import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tt", sep='	', encoding='ISO-8859-1')


offset = -1.4
i = 0
colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for col in df:
    
    if i == 0:  # for all but the first(time
        time = np.array(df[col])
    elif i==4 or i == 5 or i == 6 or i == 10:
        plt.plot(time, df[col] + i*offset, label=df[col].name, color=colors[i], alpha = 1)
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
        
    elif i == 13:
        plt.plot(time, -df[col]*10**4 + i*offset, label=df[col].name, color=colors[i])
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
        
    else:
        plt.plot(time, df[col] + i*offset, label=df[col].name, color=colors[i], alpha = 0.2)
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
    
    i += 1

plt.yticks([])