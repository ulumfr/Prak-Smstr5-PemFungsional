import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# TODO 1: Buat fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def group_heights(heights, interval_size):
    grouped_heights = {}
    
    for height in heights:
        group_key = (height // interval_size) * interval_size
        if group_key not in grouped_heights:
            grouped_heights[group_key] = {'interval': f"{group_key}-{group_key + interval_size - 1}", 'frequencies': 0}
        grouped_heights[group_key]['frequencies'] += 1
    
    return grouped_heights

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10
grouped_heights = group_heights(tinggi_badan, interval_size)

# TODO 3: Visualisasikan data dalam bentuk historagram
for group_key, data in sorted(grouped_heights.items()):
    print(f"Interval {data['interval']} : {data['frequencies']} orang")

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
mean_tinggi = np.mean(tinggi_badan)
std_tinggi = np.std(tinggi_badan)
x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)

plt.plot(x, norm.pdf(x, mean_tinggi, std_tinggi), label='PDF (Normal Distribution)', linewidth=2, color="red")
plt.hist(tinggi_badan, bins=range(150, 200, interval_size), density=True, label='Data')

plt.xlabel('Interval Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')
plt.legend(loc='lower left')
plt.show()
