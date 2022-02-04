rivers = {
    'Amazon': ['Brazil', 'Peru', 'Colombia', 'Ecuador', 'Bolivia', 'Venezuela'],
    'Ganges': ['India', 'Nepal', 'China', 'Bangladesh'],
    'Rio Grande': ['United States', 'Mexico'],
}
print('----Rivers and Countries they flow throught')
for k,v in rivers.items():
    print(f'The {k} river flows through the following countries {v}')
print('------Rivers only---------')
for k in rivers.keys():
    print(k)
print('-------Countries----------')
for v in rivers.values():
    print(v)