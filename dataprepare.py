import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import quandl
import datetime

#importing data

tcsdata = quandl.get('NSE/TCS', start_date = '2015-03-01' , end_date = '2016-03-01' )
infydata = quandl.get('NSE/INFY' ,start_date = '2015-03-01' , end_date = '2016-03-01')

# function for window rolling average

def window4(df):
    return df.rolling(window=4).mean()
    
def rolling10(df):
    return df.rolling(window=10).mean()
    

tcsdata['prevdayvol'] = tcsdata['Total Trade Quantity'].shift(-1)

tcsdata['volchange'] = abs((tcsdata['Total Trade Quantity']-tcsdata['prevdayvol'])/tcsdata['prevdayvol'])

# creating volume Shocks for 10%change

tcsdata['Volume_Shocks'] = pd.cut(tcsdata['volchange'], bins = [0,0.1,1], labels = ['1','0'])

tcsdata['closechange'] = abs((tcsdata['Close']-(tcsdata['Close'].shift(-1)))/(tcsdata['Close'].shift(-1)))

# creating price shocks for 2 % change


tcsdata['Price_Shocks'] = pd.cut(tcsdata['closechange'], bins = [0,0.2,1], labels = ['1','0'])
