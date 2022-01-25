"""
tranpose bertujuan untuk menukar baris menjadi sebuah kolom dan sebaliknya, pada pandas digunakan untuk merubah sebuah oreientasi data pada sebuah table
"""
import pandas as pd
nilai = pd.DataFrame({
   "KelasA":[11,12,13,14,15,16,17,18,19,20],
    "KelasB":[1,2,3,4,5,6,7,8,9,10],
    "KelasC":[21,22,23,24,25,26,27,28,29,30]
})

data_tasnpose=nilai.transpose()

print("Sebelum di transpose: \n{}".format(nilai))

print("Data setelah di transpose: \n{}".format(data_tasnpose))
