"""
atribut seringkali digunakan dalam bebrbagai manipulasi sebuah data

1.atribute head dan tail
dimana head digunakan utnuk menampilkan sebuah data teratas
dimana sebuah tail digunakan untuk menampilkan sebuah data terbawah
"""
import pandas as pd
df=pd.DataFrame({
    "Luas":[1,2,3,4,5,6,7,8,9,10],
    "Keliling":[11,12,13,14,15,16,17,18,19,20]
})
atas = df.head(3)
bawah = df.tail(3)

print("Data ascending")
print(atas)

print("Data Descending")
print(bawah)