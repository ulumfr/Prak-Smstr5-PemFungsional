# Mencari persamaan garis melalui 2 titik
def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # y = mx + c

    x1, y1 = p1
    x2, y2 = p2

    #TODO 1: tulis rumus untuk mendapatkan nilai M disini
    M = (y2 - y1) / (x2 - x1)

    #TODO 2: tulis rumus untuk mendapatkan nilai C disini
    C = y1 - M * x1

    return f"y = {M:.2f}x + {C:.2f}"

# Menentukan persamaan garis yang melalui titik A dan B
print("(Awal) Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 3), point(5, 9)))
print("\n(Nim) Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 4), point(6, 2)))
