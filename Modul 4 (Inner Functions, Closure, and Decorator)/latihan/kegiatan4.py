# Transformasi
import math

# P((x+tx), (y+ty)) 
def translasi(tx, ty):
    def transformasi_translasi(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transformasi_translasi

def dilatasi(sx, sy):
    def transformasi_dilatasi(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transformasi_dilatasi

def rotasi(sudut):
    def transformasi_rotasi(x, y):
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y
    return transformasi_rotasi

# titik p (koordinat awal)
x, y = 3, 5

# 1. Translasi
translasi_func = translasi(2, -1)
new_coord_translasi = translasi_func(x, y)
print("Koordinat setelah translasi:", new_coord_translasi)

# 2. Dilatasi
dilatasi_func = dilatasi(2, -1)
new_coord_dilatasi = dilatasi_func(x, y)
print("Koordinat setelah dilatasi:", new_coord_dilatasi)

# 3. Rotasi
rotasi_func = rotasi(30)
new_coord_rotasi = rotasi_func(x, y)
print("Koordinat setelah rotasi:", new_coord_rotasi)