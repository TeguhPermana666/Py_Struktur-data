"""
Merge adalah sebuah data dengan menggabungkan dua buah kolom yang berbeda menjadi satu dimana merge hnya dapat 
dilakukan jika semua data pada kedua table memiliki jumlah kolom yang sama
dengan menggunakan concat

"""

import pandas as py

tabel1=py.DataFrame({"Col1":[1,2,3],"Col2":[4,5,6]})
tabel2=py.DataFrame({"Col1":[10,9,8],"Col2":[7,11,21]})

print("Tabel1 \n{}\n".format(tabel1))
print("Tabel2 \n{}\n".format(tabel2))
gabungan=py.concat([tabel1,tabel2])
print("Data dari merge adalah\n {}\n".format(gabungan))
