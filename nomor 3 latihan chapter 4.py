import math
jarak = int(input("Masukkan jarak tempuh = "))
liter = jarak / 12
print("minimal pengisian bensin hingga penuh adalah",liter,"liter")
print("Jika bensin awal masih kosong")
isi = liter / 50
print("Minimal mengisi bensin = ")
print(math.floor(isi))
