"""
atribute sort values digunakan untuk mengurutkan atau mengsorting sebuah data
sort_values() seringkali digunakan dalam pengurutan dari besar ke kecil berdasarkan salah satu kolomnya
"""

import pandas as pd
nilai = pd.DataFrame({
   "KelasA":[11,12,13,14,15,16,17,18,19,20],
    "KelasB":[1,2,3,4,5,6,7,8,9,10],
    "KelasC":[21,22,23,24,25,26,27,28,29,30]
})

print("\nPengurutan Menurut data A")
data_sortA=nilai.sort_values(by="KelasA")
print(data_sortA)

print("\nPengurutan Menurut data B")
data_sortB=nilai.sort_values(by="KelasB")
print(data_sortB)

print("\nPengurutan Menurut data C")
data_sortC=nilai.sort_values(by="KelasC")
print(data_sortC)