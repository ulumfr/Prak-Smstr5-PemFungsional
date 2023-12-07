from functools import reduce
import matplotlib.pyplot as plt

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# TODO 1: Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# TODO 2: Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lamda)
mahasiswa = list(map(lambda x: f'{x+1}', range(len(nilai_mahasiswa))))

print('Mahasiswa\t\t\t:', mahasiswa)
print('Nilai mahasiswa\t\t\t:', nilai_mahasiswa)
print(f'Rata-rata nilai mahasiswa\t: {rata_rata:.2f}')

# TODO 3: Visualisasikan data dalam bentuk diagram batang
plt.figure(figsize=(10, 5))
plt.axhline(y=rata_rata, color='red', linestyle='dashed', linewidth=2, label=f'Rata-rata = {rata_rata:.2f}')
plt.bar(mahasiswa, nilai_mahasiswa)
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')

for i, value in enumerate(nilai_mahasiswa):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')

plt.legend()
plt.show()