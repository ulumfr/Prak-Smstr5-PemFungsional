import matplotlib.pyplot as plt
import numpy as np

# Awal
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1, label='Garis 1')
# plt.plot(y2, label='Garis 2')

# plt.title('Plot Dua Garis')
# plt.xlabel('Nilai x')
# plt.ylabel('Nilai y')

# plt.legend()
# plt.show()

# Modifikasi
garis1 = np.array([3, 8, 1, 10])
garis2 = np.array([6, 2, 7, 11])
garis3 = np.array([9, 2, 4, 7])

plt.plot(garis1, label='Garis 1', marker= 's', color='magenta', linestyle=':')
plt.plot(garis2, label='Garis 2', marker='o', color='black', linestyle='-.')
plt.plot(garis3, label='Garis 3', marker='*', color='green', linestyle='-')

plt.title('Plot Tiga Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()