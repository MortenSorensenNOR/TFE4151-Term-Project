import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


corners = ["tt", "ff", "ss", "fs", "sf"]
neg20   = ["export 2/" + s + "-20" for s in corners]
plus27   = ["export 2/" + s + "27" for s in corners]
plus50   = ["export 2/" + s + "50" for s in corners]

# 3 lists (per temperature)   of 5 dataframes (per corner)
T1 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in neg20]
T2 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in plus27]
T3 = [pd.read_csv(file, sep='	', encoding='ISO-8859-1') for file in plus50]

TS = [T1, T2, T3]
#print(TS[0])

"""
####################### ALL COLUMNS IN THE CSVS FROM BITCELL ################################

time	time	        v(vdd)     v(rw)	 v(wordline)	v(i)	    v(bitcarry)	v(t6)	
v(1:t)	v(t1)	        v(rwtemp)  v(t7)	 v(2:t)	        v(t4)	    v(t8)	    v(3:t)	
v(t2)	v(iinv)	        v(t9)	   v(4:t)	 v(t3)	        v(5:t)	    v(q)	    v(qinv)	
v(6:t)	v(7:yinv)       v(7:t)	   v(t5)	 v(8:t)	        v(8:yinv)	v(bitout)	i(v_bitcarry)	
i(v_i)	i(v_wordline)	i(v_rw)	   i(v_vss)	 i(v_vdd)
"""

def plotAll():
    al = 0.2
    AL = 1
    # Colomns we want plotted and the alpha of the line
    desiredColumns = [#("v(vdd)", al), 
                      ("v(rw)", AL), 
                      ("v(wordline)", AL), 
                      ("v(i)", AL), 
                      ("v(t1)", al), 
                      ("v(t2)", al), 
                      ("v(t3)", al), 
                      ("v(q)", al), 
                      ("v(qinv)", AL),
                      ("v(bitout)", al)
                      ]
    
    
    shift = 0.6
    colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    time = np.array(TS[0][0].time)  # make a numpy array of the time-array (its the same for everything) so indexes actually work
    for k in range(len(TS)): #temperature
        for j in range(0,5): # corners
        
            plt.subplot(3,5, j+1 + 5*k )
            if k == 0: plt.title(corners[j]) # print ff, fs, ss etc on title of top row
            
            for i in range(len(desiredColumns)):   # columns/nets
                if j == 0: 
                    if k == 0: ylabel_obj = plt.ylabel("-20°C", rotation=0)
                    if k == 1: ylabel_obj = plt.ylabel("27°C",  rotation=0)
                    if k == 2: ylabel_obj = plt.ylabel("50°C",  rotation=0)  # print temperature on ylabel of first column
                if k != 2: plt.xticks([])          # only bottom row has ticks, to make it compact
                else: plt.xlabel("t [ns]")         # put scale on bottom row
                ylabel_obj.set_horizontalalignment('right')  # Align to the right (optional)
                ylabel_obj.set_position((-1, 0.5)) 
                
                
                # plot the line and the name of the net
                plt.text(0, -(shift*i - 0.1), desiredColumns[i][0], fontsize = 8, color=colors[i])
                plt.plot(  TS[k][j].time*10**9,   TS[k][j][desiredColumns[i][0]] - shift*i,   alpha = desiredColumns[i][1], color=colors[i])
                
                # remove value on y-axs, since it makes no sense with the offsets
                plt.yticks([])
                
                # plot two dashed lines at 0 and vdd            
                plt.plot([0, time[-1]*10**9], [-shift*i, -shift*i], color=colors[i], alpha=0.2, linestyle='dashed')
                plt.plot([0, time[-1]*10**9], [-shift*i+TS[k][j]["v(vdd)"][10], -shift*i+TS[k][j]["v(vdd)"][10]], color=colors[i], alpha=0.2, linestyle='dashed')
    
    plt.rcParams["figure.figsize"]=(40,24)            
    plt.subplots_adjust(
        top=0.975,    # Distance of the top of the subplots from the top of the figure
        bottom=0.06,  # Distance of the bottom of the subplots from the bottom of the figure
        left=0.04,    # Distance of the left of the subplots from the left of the figure
        right=0.995,  # Distance of the right of the subplots from the right of the figure
        hspace=0.025, # The amount of height reserved for space between subplots
        wspace=0.01   # The amount of width reserved for space between subplots
    )
    #plt.tight_layout(False)
    plt.savefig('corners2.png', dpi=300)
    
    
    
    
    
def plotOne(k, j):  # temperature, corner
    al = 0.2
    AL = 1
    # Colomns we want plotted and the alpha of the line
    desiredColumns = [#("v(vdd)", al), 
                      ("v(rw)", AL), 
                      ("v(wordline)", AL), 
                      ("v(i)", AL), 
                      ("v(t1)", al), 
                      ("v(t2)", al), 
                      ("v(t3)", al), 
                      ("v(q)", al), 
                      ("v(qinv)", AL),
                      ("v(bitout)", al),
                      ("i(v_vdd)", AL)
                      ]
    
    
    shift = 0.6
    colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    time = np.array(TS[0][0].time)  # make a numpy array of the time-array (its the same for everything) so indexes actually work
    plt.title(corners[j])              # print ff, fs, ss etc on title of top row
    
    for i in range(len(desiredColumns)): # columns/nets
        if j == 0: 
            if k == 0: ylabel_obj = plt.ylabel("-20°C", rotation=0)
            if k == 1: ylabel_obj = plt.ylabel("27°C",  rotation=0)
            if k == 2: ylabel_obj = plt.ylabel("50°C",  rotation=0)  # print temperature on ylabel of first column
        ylabel_obj.set_horizontalalignment('right')  # Align to the right (optional)
        ylabel_obj.set_position((-1, 0.5)) 
        plt.xlabel("t [ns]")                         # put scale on bottom row
        
        if desiredColumns[i][0] != "i(v_vdd)":
            # plot the line and the name of the net
            plt.text(0, -(shift*i - 0.1), desiredColumns[i][0], fontsize = 8, color=colors[i])
            plt.plot(  TS[k][j].time*10**9,   TS[k][j][desiredColumns[i][0]] - shift*i,   alpha = desiredColumns[i][1], color=colors[i])
            
            # remove value on y-axs, since it makes no sense with the offsets
            plt.yticks([])
            
            # plot two dashed lines at 0 and vdd            
            plt.plot([0, time[-1]*10**9], [-shift*i, -shift*i], color=colors[i], alpha=0.2, linestyle='dashed')
            plt.plot([0, time[-1]*10**9], [-shift*i+TS[k][j]["v(vdd)"][10], -shift*i+TS[k][j]["v(vdd)"][10]], color=colors[i], alpha=0.2, linestyle='dashed')
        else:
            plt.text(0, -(shift*i - 0.3), desiredColumns[i][0], fontsize = 8, color="red")
            plt.plot(  TS[k][j].time*10**9,   TS[k][j][desiredColumns[i][0]]*(-10**4) - shift*i,   alpha = desiredColumns[i][1], color="red")
            
            
    plt.rcParams["figure.figsize"]=(40,24) 
    plt.savefig('simulation2.png', dpi=300)






def rms(arr):
    return np.sqrt(np.mean(np.square(arr)))

def plotPower():
    al = 0.2
    AL = 1
    # Colomns we want plotted and the alpha of the line
                      
    slic1 = [4900,6900]
    slic2 = [22900,25000]
    
    shift = 0.6
    colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    time = np.array(TS[0][0].time)*10**9  # make a numpy array of the time-array (its the same for everything) so indexes actually work
    
    outTable = np.zeros((3,5,2))
    
    for k in range(len(TS)): #temperature
        for j in range(0,5): # corners
        
            plt.subplot(3,5, j+1 + 5*k )
            if k == 0: plt.title(corners[j]) # print ff, fs, ss etc on title of top row
            if k != 2: plt.xticks([])          # only bottom row has ticks, to make it compact
            else: plt.xlabel("t [ns]")         # put scale on bottom row
            
            
            if j == 0: 
                if k == 0: ylabel_obj = plt.ylabel("-20°C\n i [uA]",  rotation=0)
                if k == 1: ylabel_obj = plt.ylabel("27°C \n i [uA]",  rotation=0)
                if k == 2: ylabel_obj = plt.ylabel("50°C \n i [uA]",  rotation=0)  # print temperature on ylabel of first column
            else: plt.yticks([])
            ylabel_obj.set_horizontalalignment('right')  # Align to the right (optional)
            ylabel_obj.set_position((0.5, 0.5)) 
            
            
            
            current = np.array(TS[k][j]["i(v_vdd)"])
            voltage = np.array(TS[k][j]["v(vdd)"]) 
            
            prms1 = rms(current[slic1[0]:slic1[1]])*rms(voltage[slic1[0]:slic1[1]]) * 10**6  # power in micro-watts
            prms2 = rms(current[slic2[0]:slic2[1]])*rms(voltage[slic2[0]:slic2[1]]) * 10**6 
            
            outTable[k][j] = [prms1, prms2]
            
            # whole current graph
            plt.plot(  time[0:slic1[0]],          current[0:slic1[0]]* 10**6,         color="orangered")
            plt.plot(  time[slic1[1]:slic2[0]],   current[slic1[1]:slic2[0]]* 10**6,  color="orangered")
            plt.plot(  time[slic2[1]:-1],         current[slic2[1]:-1]* 10**6,        color="orangered")
            
            # yellow on measured parts
            plt.plot(  time[slic1[0]:slic1[1]], current[slic1[0]:slic1[1]]* 10**6, alpha = 1, color = "teal", label=f"P at 0: {round(prms1,3)}uW")
            plt.plot(  time[slic2[0]:slic2[1]], current[slic2[0]:slic2[1]]* 10**6, alpha = 1, color = "aqua",      label=f"P at 1: {round(prms2,3)}uW")
            
            plt.ylim(-10.1, 10.1)
            plt.legend(loc="lower left")
            
            
    plt.rcParams["figure.figsize"]=(42,24)            
    plt.subplots_adjust(
        top=0.975,    # Distance of the top of the subplots from the top of the figure
        bottom=0.06,  # Distance of the bottom of the subplots from the bottom of the figure
        left=0.04,    # Distance of the left of the subplots from the left of the figure
        right=0.995,  # Distance of the right of the subplots from the right of the figure
        hspace=0.05, # The amount of height reserved for space between subplots
        wspace=0.01   # The amount of width reserved for space between subplots
    )
    plt.savefig('power2.png', dpi=300)
    plt.tight_layout()
    
    return outTable
 

   

def plotTransition():
    # Colomns we want plotted and the alpha of the line
    desiredColumns = [#("v(vdd)", al), 
                      #"v(rw)", 
                      "v(wordline)",
                      #"v(i)", 
                      #"v(t1)",  
                      #"v(t2)",
                      #"v(t3)",  
                      "v(q)",  
                      "v(qinv)",
                      #"v(bitout)"
                      ]
    
    
    shift  = 0.6
    colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    temps  =  ["-20 °C", "27 °C", "50 °C"]
    time   = np.array(TS[0][0].time)*10**9  # make a numpy array of the time-array (its the same for everything) so indexes actually work
    for k in range(len(TS)): #temperature
        for j in range(0,5): # corners
        
            plt.subplot(1,5, j+1 )
            if k == 0: plt.title(corners[j]) # print ff, fs, ss etc on title of top row
            
            if j == 0: 
                ylabel_obj = plt.ylabel("V",  rotation=0)
            else:
                # remove value on y-axs, since it makes no sense with the offsets
                plt.yticks([])
            ylabel_obj.set_horizontalalignment('right')  # Align to the right (optional)
            ylabel_obj.set_position((-3, 0.5)) 
                
                
            plt.xlabel("t [ns]")         # put scale on bottom row
            
            
            
            
            
            # plot two dashed lines at 0 and vdd            
            plt.plot([0, time[-1]], [0, 0], color="black", alpha=0.2, linestyle='dashed')
            plt.plot([0, time[-1]], [TS[k][j]["v(vdd)"][10], TS[k][j]["v(vdd)"][10]], color="black", alpha=0.2, linestyle='dashed')
            
            plt.plot([0, time[-1]], [TS[k][j]["v(vdd)"][10]*0.8, TS[k][j]["v(vdd)"][10]*0.8], color="black", alpha=0.2, linestyle='dashed')
            plt.plot([0, time[-1]], [TS[k][j]["v(vdd)"][10]*0.2, TS[k][j]["v(vdd)"][10]*0.2], color="black", alpha=0.2, linestyle='dashed')
            
            # plot the lines
            plt.plot(  time,   TS[k][j][desiredColumns[0]], color="black"  )
            plt.plot(  time,   TS[k][j][desiredColumns[1]], color=colors[k])
            plt.plot(  time,   TS[k][j][desiredColumns[2]], color=colors[k], label=temps[k])
            
            plt.plot( [65.02,65.02], [-3, 3] , color = "red", linestyle = "dashed")
            plt.plot( [68.02,68.02], [-3, 3] , color = "red", linestyle = "dashed")
            
            
            plt.xlim(64.5, 70)
            plt.ylim(-0.1, 0.5)
            plt.legend(loc="lower right")
            
                
    plt.rcParams["figure.figsize"]=(50,9)            
    plt.subplots_adjust(
        top=0.975,    # Distance of the top of the subplots from the top of the figure
        bottom=0.06,  # Distance of the bottom of the subplots from the bottom of the figure
        left=0.04,    # Distance of the left of the subplots from the left of the figure
        right=0.995,  # Distance of the right of the subplots from the right of the figure
        hspace=0.025, # The amount of height reserved for space between subplots
        wspace=0.06   # The amount of width reserved for space between subplots
    )
    #plt.tight_layout(False)
    plt.savefig('transition2.png', dpi=300)
    

#plotOne(1,0)
#plotAll()
#print(plotPower())
plotTransition()