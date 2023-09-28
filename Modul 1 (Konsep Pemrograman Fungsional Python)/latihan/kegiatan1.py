# Definisikan Fungsi Pohon
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))

# Fungs Pertambahan
def add(kiri, kanan):
    return kiri + kanan

# Fungsi Pengurangan
def minus(kiri, kanan):
    return kiri - kanan

# Fungsi Perkalian
def mult(kiri, kanan):
    return kiri * kanan

# Fungsi Pembagian
def div(kiri, kanan):
    return kiri / kanan

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)