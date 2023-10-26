random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_data = tuple(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

intdata_mapped = list(map(lambda x: {'ratusan': x // 100, 'puluhan': (x % 100) // 10, 'satuan': x % 10}, int_data))

print("Data Float :", float_data)
print("Data Int :")
for item in intdata_mapped:
    print(item)
print("Data String :", string_data)
