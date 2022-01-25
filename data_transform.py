import pandas as pd
"""
Data transform adalah sebuah kegiatan untuk pengolahan data
 
"""

nilai_siswa ={"Andi":[80,77,54],"Ando":[92,45,67],"Malika":[30,70,100]}
df=pd.DataFrame.from_dict(nilai_siswa)
print(df)
df=pd.DataFrame.from_dict(nilai_siswa,orient="index",columns=["Matematika","Biologi","Bahasa_Indonesia"])
print(df)

#transformasi sebuah tabel data sehingga nanti ada dua kolom yakni rata-rata dan rangking
#axis =1 =>baris
#axis =0 =>kolom

#Rataam
import numpy as py
df["Rata-Rata"]=df.apply(py.mean,axis=1)
print(df)

#Rangkingan
df["Rangking"]=df["Rata-Rata"].rank()
df["Rangking"]=df["Rangking"].apply(lambda x : int(x))
print(df)

