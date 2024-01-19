# 2024-01-15_monday
# 2024-01-17_wednesday
# 2024-01-17_thursday
#
# Polish postal codes generator 1.2
# Tomasz Mering, CODE2.0, 2024

kod1 = "79-900"
kod2 = "80-155"

# transform kod1 and kod2 string variables into ints
kod1 = int(kod1.replace('-',''))
kod2 = int(kod2.replace('-',''))

# print(kod1, kod2)
# print('\n')

lista_kodow = map(str, range(kod1, (kod2 + 1)))

# print(lista_kodow)
# print('\n')

lista_kodow = list(map(lambda e : (e[0:2] + '-' + e[2:5]), lista_kodow))

print(lista_kodow)
