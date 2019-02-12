import pandas as pd
import pandas_datareader as pdr
from datetime import date
from dateutil.relativedelta import relativedelta

# ch = pd.read_csv("~/Downloads/california_housing_train.csv", delimiter=',')
# print(ch.columns)

goog = pdr.get_data_yahoo("GOOG", date.today() + relativedelta(months=-3))
print(goog.columns)
print(goog.describe())
