"""
Atribute describe digunakan untuk menampilkan sebuah data statistik yakni rata rata nilai minimum, nilai maksimum, standar deviasi, dan nilai kuartil dari DataFrame
"""
import pandas as pd

nilai = pd.DataFrame({
   "KelasA":[11,12,13,14,15,16,17,18,19,20],
    "KelasB":[1,2,3,4,5,6,7,8,9,10],
    "KelasC":[21,22,23,24,25,26,27,28,29,30]
})
data_statistik=nilai.describe()
print(data_statistik)