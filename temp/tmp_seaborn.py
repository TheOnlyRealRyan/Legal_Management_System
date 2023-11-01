
"""
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import grab_from_db as db


def create_plot():
    sns.set(style="white")

    # Generate a large random dataset
    dataset = db.all_case_data()
    print(dataset)
    time = []
    for i in dataset: 
        time.append(i[7]) 
    print(time)
    rs = np.random.RandomState(33)
    d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                     columns=list(ascii_letters[26:]))

    # Compute the correlation matrix
    corr = d.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool_)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    return f

# --- main ---

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

label = tkinter.Label(root, text="Matplotlib with Seaborn in Tkinter")
label.pack()

fig = create_plot()

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack()

button = tkinter.Button(root, text="Quit", command=root.destroy)
button.pack()

tkinter.mainloop()
"""

import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pylab as plt
# make epoch datetime
list_date = ['2020-01-01', '2019-01-02', '2018-01-15', '2017-01-18']
dates = [pd.to_datetime(d) for d in list_date]
dates_epoch = [(t- pd.Timestamp("1970-01-01")) // pd.Timedelta('1ms') for t in dates]
# create dataframe
df_sub = pd.DataFrame([dates_epoch, 
                       [2019, 2018, 2017, 2016], 
                       [15, 9, 39, 20]
                      ])
df_sub = df_sub.T
df_sub.columns=['GAME_DATE', 'SEASON', 'PTS']
# print(df_sub)
#        GAME_DATE  SEASON  PTS
# 0  1577836800000    2019   15
# 1  1546387200000    2018    9
# 2  1515974400000    2017   39
# 3  1484697600000    2016   20
sns.lmplot(x='GAME_DATE', y='PTS', hue= 'SEASON', data=df_sub,lowess=True)
# get current axis
ax = plt.gca()
# get current xtick labels
xticks = ax.get_xticks()
# convert all xtick labels to selected format from ms timestamp
ax.set_xticklabels([pd.to_datetime(tm, unit='ms').strftime('%Y-%m-%d') for tm in xticks], rotation=50)
plt.show()