import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

corners = ["tt", "ff", "ss", "fs", "sf"]
neg20   = ["proper/" + s + "_-20" for s in corners]
plus27   = ["proper/" + s + "_27" for s in corners]
plus50   = ["proper/" + s + "_50" for s in corners]

T1 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in neg20]
T2 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in plus27]
T3 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in plus50]


def plot(pandaThingy, a, mul = 1):
    graph = np.array(pandaThingy)*mul
    plt.plot(time, graph + offs*offset, label=pandaThingy.name, color=colors[i], alpha = a)
    plt.text(0, offs*offset+0.4, pandaThingy.name, fontsize = 5, color=colors[i])
    plt.plot([0, time[-1]], [offs*offset, offs*offset], color=colors[i], alpha=0.2, linestyle='dashed')
    plt.plot([0, time[-1]], [offs*offset+1, offs*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')


offset = -1.4

colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for j in range(len(neg20)):
    plt.subplot(3,5,j+1)
    plt.yticks([])
    plt.xticks([])
    plt.title(corners[j])
    i = 0
    offs = 0
    for col in T1[j]:
        # getting time table
        if i == 0:  
            time = np.array(T1[j][col])*10**9   
            i += 1
        
        # skipline
        elif i == 1 or i == 7 or i == 8 or i == 9 or i == 11:  
            i += 1
        
        # interesting lines
        elif i == 5 or i == 6 or i == 10:   
            plot(T1[j][col], 1)
            i += 1
            offs += 1
            
        # amplified lines   
        elif i == 13:
            plot(T1[j][col], 1, -10**3.5)
            i += 1
            offs += 1
        
        # the rest
        else: 
            plot(T1[j][col], 0.2)
            i += 1
            offs += 1
        
for j in range(len(plus27)):
    plt.subplot(3,5,j+6)
    plt.yticks([])
    plt.xticks([])
    i = 0
    offs = 0
    for col in T2[j]:
        # getting time table
        if i == 0:  
            time = np.array(T2[j][col])*10**9   
            i += 1
        
        # skipline
        elif i == 1 or i == 7 or i == 8 or i == 9 or i == 11:  
            i += 1
        
        # interesting lines
        elif i == 5 or i == 6 or i == 10:   
            plot(T2[j][col], 1)
            i += 1
            offs += 1
            
        # amplified lines   
        elif i == 13:
            plot(T2[j][col], 1, -10**3.5)
            i += 1
            offs += 1
        
        # the rest
        else: 
            plot(T2[j][col], 0.2)
            i += 1
            offs += 1        


for j in range(len(plus50)):
    plt.subplot(3,5,j+11)
    plt.yticks([])
    plt.xlabel("t [ns]")
    i = 0
    offs = 0
    for col in T3[j]:
        # getting time table
        if i == 0:  
            time = np.array(T3[j][col])*10**9   
            i += 1
        
        # skipline
        elif i == 1 or i == 7 or i == 8 or i == 9 or i == 11:  
            i += 1
        
        # interesting lines
        elif i == 5 or i == 6 or i == 10:   
            plot(T3[j][col], 1)
            i += 1
            offs += 1
            
        # amplified lines   
        elif i == 13:
            plot(T3[j][col], 1, -10**3.5)
            i += 1
            offs += 1
        
        # the rest
        else: 
            plot(T3[j][col], 0.2)
            i += 1
            offs += 1 
            
plt.rcParams["figure.figsize"]=(40,24)            
plt.subplots_adjust(
    top=0.975,    # Distance of the top of the subplots from the top of the figure
    bottom=0.06,  # Distance of the bottom of the subplots from the bottom of the figure
    left=0.04,   # Distance of the left of the subplots from the left of the figure
    right=0.995,  # Distance of the right of the subplots from the right of the figure
    hspace=0.025, # The amount of height reserved for space between subplots
    wspace=0.01   # The amount of width reserved for space between subplots
)
plt.savefig('corners.png', dpi=300)
