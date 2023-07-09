# -*- coding: utf-8 -*-
"""python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZwcztBbH4xzpVw_SWJJTBRwdXgB421P?usp=sharing
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""- library -
1. import pandas berfungsi sebagai penghubung eksternal, contohnya ingin mengambil file csv.
2. import numpy berfungsi untuk mengelola komputasi matriks dalam hal ini phyton.
3. import matplotlib.pyplot berfungsi untuk merepresenrasikan data berupa grafik.
4. import seaborn berfungsi untuk visualisasi data yang dibangun di atas matplotlib. 
"""

import pandas as pd

data = pd.read_csv("./Algorithm_data_mentah.csv")
data

"""Memasukkan dataset Tingkat Kepuasan Pelanggan"""

x = data.iloc[:, [0, 1, 2, 3, 4]].values
y = data.iloc[:, -1].values

"""Membagi data x dan data y"""

print(x)

"""Menampilkan data x"""

print(y)

"""Menampilkan data y"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.20, random_state = 0)

"""Memisahkan dataset menjadi data training dan data testing"""

print(x_train)

"""Mencetak x_train"""

len(x_train)

"""Mencetak banyaknya data x_train"""

len(x)

"""Mencetak banyaknya data x"""

len(x_test)

"""Mencetak banyaknya data x_test"""

len(y)

"""Mencetak banyaknya data y"""

len(y_test)

"""Mencetak banyaknya data y_test"""

len(y_train)

"""Mencetak banyaknya data y_train"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

"""Tahap preprocessing"""

print(x_train)

"""Hasil normalisasi Data x_train"""

print(x_test)

"""hasil normalisasi data x_test"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
classifier.fit(x_train, y_train)

"""klasifikasi dengan K-NN"""

y_prediksi = classifier.predict(x_test)

"""prediksi terhadap hasil klasifikasi"""

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_prediksi)
print(cm)

"""hasil akurasi didapat dari a= a11+a33/total keseluruhan matriks
hasil pembagian dikali 100%.

Untuk akurasi di atas didapati hasilnya 13+0/20 = 0.65 * 100% = 0,65

"""