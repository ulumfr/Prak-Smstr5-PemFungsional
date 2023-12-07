import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ('Produk A', 50, 10),
    ('Produk B', 30, 25),
    ('Produk C', 20, 30),
    ('Produk D', 60, 8),
    ('Produk E', 40, 15),
    ('Produk F', 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk viusalisasi pertama
nama_produk = list(map(lambda x: x[0], data_transaksi))
harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

print('Nama Produk\t:', nama_produk)
print('Harga Produk\t:', harga_produk)
print('Jumlah Terjual\t:', jumlah_terjual)

plt.figure(figsize=(12, 6))

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual, label='Hubungan')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.legend()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = np.array(harga_produk) * np.array(jumlah_terjual)
# pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
plt.subplot(1, 2, 2)
plt.bar(nama_produk, pendapatan_produk, label='Pendapatan', color='skyblue')
plt.title('Pendapatan Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk')
plt.legend()

for i, value in enumerate(pendapatan_produk):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')

plt.show()