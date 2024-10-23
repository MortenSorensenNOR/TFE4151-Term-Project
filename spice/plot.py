import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
                # v-- filename
df = pd.read_csv("tt", sep='	', encoding='ISO-8859-1')


offset = -1.4  # offset between lines (in unit of volts, hehe)
i = 0          # iterator
colors =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for col in df:
    # guuhh, mye som skjer her. Acsessing av columns i pandas er weird, så bruker en incrementer, i
    # also veldig mye gjentagende kode, men dgb, hehe.
    # første iffen lagrer første kolonne i en forståelig datatype, siden vi trenger den ofte
    # den andre iffen plotter noen av grafene i en linje med full opacity (else til slutt plotter resten med en lavere opacity)
    # tredje iffen er brukt til å skalere opp strømmen, siden vi fikk den i nanoamper (????). 
    # Indexene her er hardkoda, så de funker bare hvis du eksporterer NØYAKTIG samme data som meg, men resten er dynamisk, så du får sette indeksene som du vill
    if i == 0:  # hent ut tid
        time = np.array(df[col])
    elif i==4 or i == 5 or i == 6 or i == 10:  # plott med tykkere linje
        plt.plot(time, df[col] + i*offset, label=df[col].name, color=colors[i], alpha = 1)
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
        
    elif i == 13:  # plot tykk, og med multiplisert verdi
        plt.plot(time, -df[col]*10**4 + i*offset, label=df[col].name, color=colors[i])
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
        
    else:  # plott resten med litt gjennomsiktig linje
        plt.plot(time, df[col] + i*offset, label=df[col].name, color=colors[i], alpha = 0.2)
        plt.text(0, i*offset+0.4, df[col].name, fontsize = 10, color=colors[i])
        plt.plot([0, time[-1]], [i*offset, i*offset], color=colors[i], alpha=0.2, linestyle='dashed')
        plt.plot([0, time[-1]], [i*offset+1, i*offset+1], color=colors[i], alpha=0.2, linestyle='dashed')
    
    i += 1

plt.yticks([])
