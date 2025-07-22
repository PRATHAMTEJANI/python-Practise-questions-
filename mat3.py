#here we make label for plot
import matplotlib.pyplot as pl
import numpy as mk

x = mk.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = mk.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family' : 'serif' , 'color':'blue' , 'size' : 15}
font2 = {'family' : 'serif' , 'color':'green' , 'size' : 20}

pl.title("TITLE are here" , fontdict=font1 , loc='left')
pl.xlabel("bottom side writing area" , fontdict=font2)
pl.ylabel("top left side writing area" , fontdict=font2)

pl.plot(x,y)
pl.grid(color='green' , linestyle='--' , linewidth = 1)   # specify the axis for grid learn frm w3school
pl.show()   







