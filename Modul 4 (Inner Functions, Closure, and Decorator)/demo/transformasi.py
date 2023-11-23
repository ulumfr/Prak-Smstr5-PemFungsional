import math

def input_point(isi):
    titik = input(isi)
    x, y = map(int, titik.split())
    return x, y

def calc_gradient(a, b):
    x1, y1 = a
    x2, y2 = b
    return (y2 - y1) / (x2 - x1)

def calc_constanta(titik, gradient):
    x1, y1 = titik
    return y1 - gradient * x1

def transformation(gradient, c):
    return f"y = {gradient:.2f}x + {c:.2f}"

def decorator(transformation_func):
    def wrapper(titikA, titikB, *args):
        transformed_points = transformation_func(titikA, titikB, *args)
        return transformed_points
    return wrapper

@decorator
def translasi(titikA, titikB, tx, ty):
    x1, y1 = titikA
    x2, y2 = titikB
    return [(x1 + tx, y1 + ty), (x2 + tx, y2 + ty)]

@decorator
def rotasi(titikA, titikB, sudut):
    def rotate_point(x, y, sudut):
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y

    def rotate_line(titikA, titikB, sudut):
        x1, y1 = titikA
        x2, y2 = titikB
        x1_rotated, y1_rotated = rotate_point(x1, y1, sudut)
        x2_rotated, y2_rotated = rotate_point(x2, y2, sudut)
        return [(x1_rotated, y1_rotated), (x2_rotated, y2_rotated)]
    return rotate_line(titikA, titikB, sudut)

@decorator
def dilatasi(titikA, titikB, sx, sy):
    x1, y1 = titikA
    x2, y2 = titikB
    return [(x1 * sx, y1 * sy), (x2 * sx, y2 * sy)]

def input_user():
    print("========== TRANSFORMASI BERUNTUN ==========\n")
    titikA = input_point("Masukkan Titik A (spasi)\t: ")
    titikB = input_point("Masukkan Titik B (spasi)\t: ")
    tx = float(input("Masukkan Translasi (tx)\t\t: "))
    ty = float(input("Masukkan Translasi (ty)\t\t: "))
    sudut = int(input("Masukkan Sudut Rotasi\t\t: "))
    sx = float(input("Masukkan Faktor Skala (sx)\t: "))
    sy = float(input("Masukkan Faktor Skala (sy)\t: "))
    return titikA, titikB, tx, ty, sudut, sx, sy

def main(): 
    awalTitikA = 3, 4
    awalTitikB = 5, 6
    awalTx = 2
    awalTy = -3
    awalSudut = 60
    awalSx = 1.5
    awalSy = 2

    titikA, titikB, tx, ty, sudut, sx, sy = input_user()

    awalGradient = calc_gradient(awalTitikA, awalTitikB)
    awalConstanta = calc_constanta(awalTitikA, awalGradient)

    print("\n\n===== OUTPUT dari Modul =====")
    print("\n(AWAL) Persamaan garis yang melalui titik {} dan {}: \n".format(awalTitikA, awalTitikB), transformation(awalGradient, awalConstanta))
    
    awalTranslated_points = translasi(awalTitikA, awalTitikB, awalTx, awalTy)
    awalRotated_points = rotasi(*awalTranslated_points, awalSudut)
    awalScaled_points = dilatasi(*awalRotated_points, awalSx, awalSy)
    
    awalNewGradient = calc_gradient(awalScaled_points[0], awalScaled_points[1])
    awalNewConstanta = calc_constanta(awalScaled_points[0], awalNewGradient)

    print("(AWAL) Persamaan garis baru setelah transformasi: \n", transformation(awalNewGradient, awalNewConstanta))
    print("\n(AWAL) Hasil Translasi\t\t:", [(int(x), int(y)) for x, y in awalTranslated_points])
    print("(AWAL) Hasil Rotasi\t\t:", awalRotated_points)
    print("(AWAL) Hasil Perbesaran Skala\t:", awalScaled_points)
    
    gradient = calc_gradient(titikA, titikB)
    constanta = calc_constanta(titikA, gradient)

    print("\n\n===== OUTPUT dari NIM =====")
    print("\nPersamaan garis yang melalui titik {} dan {}: \n".format(titikA, titikB), transformation(gradient, constanta))

    translated_points = translasi(titikA, titikB, tx, ty)
    rotated_points = rotasi(*translated_points, sudut)
    scaled_points = dilatasi(*rotated_points, sx, sy)
    
    newGradient = calc_gradient(scaled_points[0], scaled_points[1])
    newConstanta = calc_constanta(scaled_points[0], newGradient)

    print("Persamaan garis baru setelah transformasi: \n", transformation(newGradient, newConstanta))
    print("\nHasil Translasi\t\t:", [(int(x), int(y)) for x, y in translated_points])
    print("Hasil Rotasi\t\t:", rotated_points)
    print("Hasil Perbesaran Skala\t:", scaled_points)
if __name__ == '__main__':
    main()