# Penerapan Closure dengan Currying
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan # mengembalikan fungsi inner operator

# 1. HOF
kali = perkalian(4)
hasil = kali(6)
print("HASIL HOF : ", hasil)

# 2. Currying
hasil = perkalian(2)(5)
print("\nHASIL CURRYING : ", hasil)