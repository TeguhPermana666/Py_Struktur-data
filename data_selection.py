import pandas as pd
"""
Data Selection adalah sebuah cara dalam pengambalian sebuah data dari sebuah table 
data slicing dan data indexing 
"""
jenis_tanaman=["Mawar","Melati","Anggrek","Cempaka","Putin","Lenin"]
harga10=[20000,30000,50000,60000,90000,100000]
harga100=[100000,200000,300000,400000,500000,900000]
gabungan=list(zip(jenis_tanaman,harga10,harga100))
print(gabungan)

data=pd.DataFrame(gabungan,columns=["Jenis","10","100"])
print(data)

"""
Data indexing adalah sebuah proses pengambilan data dari sebuah index data dari baris or kolom secara spesifik 
 
 loc[] 
 illoc[]

1.loc
mengambil sebuah baris tertentu dalam sebuah tabel dengan mengsepesifikasikan nama kolomnya 
"""
data_ambbil=data.loc[[0,4]]
print(data_ambbil)

"""
2.iloc
hampir sama dengan loc sama sama pengambilan data dari indexnya 
"""
data_ambbil2=data.iloc[[2,3]]
print(data_ambbil2)

"""
Data slicing
sebuah proses pemotongan data prosesnya hampir sama dengan pemotongan data pada biasanya
"""
print("\n\nData Slicing")
data_slicing=data[2:4]
print(data_slicing)