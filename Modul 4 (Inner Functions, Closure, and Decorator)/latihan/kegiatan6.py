# Mencari persamaan garis melalui 1 titik
def point(x, y):
    return x, y

def line_equation_of(p1, M):
    #TODO 1: gunakan inner function dan closure untuk menghitung nilai C
    def calculate_C():
        x1, y1 = p1
        return y1 - M * x1 
        
    #TODO 2: panggil fungsi inner untuk mendapatkan nilai C
    C = calculate_C()

    return f"y = {M:.2f}x + {C:.2f}"

print("(Awal) Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
print(line_equation_of(point(6, -2), -2))
print("\n(NIM) Persamaan garis yang melalui titik (4,6) dan bergradien 2:")
print(line_equation_of(point(4, 6), 2))