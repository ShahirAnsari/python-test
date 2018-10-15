import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import quandl
import datetime
from pandas import Series

from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.transform import linear_cmap
from bokeh.palettes import Spectral
from bokeh.models import ColumnDataSource, ColorBar

tcsdata = quandl.get('NSE/TCS', start_date = '2015-03-01' , end_date = '2016-03-01' )

#  A - plot of close prices of stocks/indices (graph A)

p = figure(plot_width=400, plot_height=400)
p.patch(tcsdata.index,tcsdata.Close, alpha=0.5, line_width=2)
show(p)

#  B - plot based on difference of 52 week moving average (Grapf B)

source1 = ColumnDataSource(dict(x=tcsdata.Open,y=tcsdata.Close))
a = figure(plot_width=500, plot_height=500, title="Linear Color Map Based on Y")
x = tcsdata.Open
y = tcsdata.Close
mapper = linear_cmap(field_name='y', palette=['blue'],low=min(y) ,high=max(y))
a.circle(x='x', y='y', line_color=mapper,color=mapper, fill_alpha=1, size=12, source=source1)
color_bar = ColorBar(color_mapper=mapper['transform'], width=8,  location=(0,0))
a.add_layout(color_bar, 'right')
show(a)


#  C - closing Pricing shock without volume shock to identify volumeless price movement (Graph C)
difference = tcsdata.Close - window4(tcsdata).Close
difference.head()

c = figure(plot_width=400, plot_height=400)
c.patch(tcsdata.index,difference, alpha=0.5, line_width=2,color = 'blue')
show(c)


# D - autocorrelation (Graph D)
closingseries = tcsdata.Close
plot_acf(closingseries)

pyplot.show()

