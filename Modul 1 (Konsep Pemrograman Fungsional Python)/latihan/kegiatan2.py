# Data Random List
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dictionary = {}
float_tuple = ()
string_list = []

for data in random_list:
    # Data int disimpan ke dictionary
    if isinstance(data, int):
        satuan = data % 10
        puluhan = (data // 10) % 10
        ratusan = data // 100
        int_dictionary[data] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}

    # Data float disimpan ke tuple
    elif isinstance(data, float):
        float_tuple += (data,)

    # Data string disimpan ke list
    elif isinstance(data, str):
        string_list.append(data)

print("Integer Dictionary:", int_dictionary, end='\n\n')
print("Float Tuple:", float_tuple, end='\n\n')
print("String List:", string_list, end='')