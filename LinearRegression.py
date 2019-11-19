#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.Veri Onisleme

#2.1. Veri Yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")
print(veriler)
aylar = veriler[['Aylar']]
print(aylar)
satislar = veriler[['Satislar']]
print(satislar)

#Verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)


#Verilerin olceklenmesi(Standarlaştırma yapılmıştır)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#Model inşaası(linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)# fit: create edilen nesneden X_train ve Y_train bilgilerini
# alarak bir model olusturulmasını sağlıyor. X_train en Y_train i  öğrenmesini bekliyoruz.s

tahmin = lr.predict(x_test) # X_test'ten Y_test'i doğru tahmin edebilecek mi ?
x_train = x_train.sort_index()
y_train = y_train.sort_index()

#linear regression görselleştirme
plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))

plt.title("Aylara Göre Satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
