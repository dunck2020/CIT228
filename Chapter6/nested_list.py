rivers = {
    'Amazon': ['Brazil', 'Peru', 'Colombia', 'Ecuador', 'Bolivia', 'Venezuela'],
    'Ganges': ['India', 'Nepal', 'China', 'Bangladesh'],
    'Rio Grande': ['United States', 'Mexico'],
}

for key, value in rivers.items():
    print(f"The {key.title()} river flows through: ")
    for v in value:
        print("\t\t\t\t",v)

