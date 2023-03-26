#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time

#import the data
data = pd.read_csv("Data Clean.csv")
image = Image.open("house-harga.jpg")
st.title("Selamat Datang di Aplikasi Prediksi Harga Rumah di Jakarta Selatan")
st.image(image, use_column_width=True)

#checking the data
st.write("Ayo prediksi harga rumah yang akan Anda beli di kota Jakarta Selatan!")
check_data = st.checkbox("Lihat contoh data")
if check_data:
    st.write(data[1:10])
st.write("Sekarang ayo lihat berapa harga nya dengan memilih beberapa parameterNow let's find out how much the hargas when we choosing some parameters.")

#input the numbers
sqft_liv = st.slider("Berapa luas bangunan rumahnya?",int(data.sqft_living.min()),int(data.sqft_living.max()),int(data.sqft_living.mean()) )
sqft_abo = st.slider("Berapa luas tanahnya?",int(data.sqft_above.min()),int(data.sqft_above.max()),int(data.sqft_above.mean()) )
bath     = st.slider("Berapa banyak kamar tidur?",int(data.bathrooms.min()),int(data.bathrooms.max()),int(data.bathrooms.mean()) )
view = st.slider("Berapa banyak kamar mandi",int(data.view.min()),int(data.view.max()),int(data.view.mean()) )
sqft_bas   = st.slider("Berapa luas garasi mobil?",int(data.sqft_basement.min()),int(data.sqft_basement.max()),int(data.sqft_basement.mean()) )
condition  = st.slider("Ada berapa lantai rumahnya?",int(data.condition.min()),int(data.condition.max()),int(data.condition.mean()) )

#splitting your data
X = data.drop('harga', axis = 1)
y = data['harga']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#Linear Regression model
#import your model
model=LinearRegression()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = model.predict([[sqft_liv,sqft_abo,bath,view,sqft_bas,condition]])[0]
akurasi= np.sqrt(r2_score(y_test,model.predict(X_test)))


#checking prediction house harga
if st.button("Submit"):
    st.header("Prediksi harga rumah adalah: Rp. {}".format(int(predictions)))
    st.subheader("Range prediksinya adalah dari Rp.{} hingga Rp. {}".format(int(predictions-errors),int(predictions+errors) ))
    st.subheader("Akurasi : {}".format(akurasi))
