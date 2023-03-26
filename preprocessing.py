#importing the package
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import statsmodels.regression.linear_model as sm

#importing the data
dataset = pd.read_csv('data.csv')

#encoding categorical data
labelEncoder_X = LabelEncoder()
dataset[:,13]= labelEncoder_X.fit_transform(dataset[:,13])
onehotencoder = OneHotEncoder(categorical_features=[13])
dataset = onehotencoder.fit_transform(dataset).toarray()

#avoiding the dummy variable trap
dataset=dataset[:, 1:]

#select best variable with high correlation
dataset.corr()[43].sort_values()


data.columns

# how many data we have
data.shape

#checking harga range
data.harga.describe()

#to view better number, not with e-
pd.set_option('display.float_format', lambda x: '%.2f' % x)


data[data.harga == 26590000]


data.sort_values('harga', ascending=False).head(10)

data.corr()['harga'].sort_values()

data[['harga', 'luas_bangunan', 'luas_tanah', 'jumlah_kamar_tidur', 'jumlah_kamar_mandi', 'luas_garasi']].head()

print(data.columns)
print(len(data.columns))

data[['harga']].describe()

#check what house that don't have harga (harga=0)
data[data['harga'] == 0]

#check how many data
data[data['harga'] == 0].shape[0]

#check what house that don't have harga (harga=0)
data[data['harga'] == 26590000]

#what should you do?
#in this case I will do something, drop value that not on range
iqr = data['harga'].describe()['75%'] - data['harga'].describe()['25%']
lower_bound = data['harga'].describe()['25%'] - (1.5*iqr)
upper_bound = data['harga'].describe()['75%'] + (1.5*iqr)
print("IQR equals {}".format(iqr))
print("Lower bound of harga is {}".format(lower_bound))
print("Upper bound of harga is {}".format(upper_bound))

#just go on with data itself
data_clean = data.copy()
data_clean = data[(data.harga > 0) & (data.harga <= upper_bound)]
data_clean.shape

data_clean[['harga']].describe()


+ labelEnocder_data = LabelEncoder()
data_clean[:, 13] = labelEnocder_data.fit_transform(data_clean[:,13])


data_clean.to_csv("Data Clean.csv",index=False)
