import matplotlib.pyplot as plt
import numpy as np

# Awal
# xpoints = np.array([1, 8, 10])
# ypoints = np.array([3, 10, 5])

# plt.figure(figsize=(5,5))
# plt.plot(xpoints, ypoints, color='red')

# plt.xlim([0, 16])
# plt.ylim([0, 16])
# plt.show()

# Modifikasi
xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(10, 5))
plt.plot(xpoints, ypoints, marker='*', color='hotpink', linestyle='-.', linewidth='2.5')

plt.title('Percobaan 2')
plt.xlim([0, 16])
plt.ylim([0, 16])
plt.show()