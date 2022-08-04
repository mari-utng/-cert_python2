
from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre: ")
try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    f = open(file_name + '.hist', 'wt')
    
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            f.write(char + ' -> ' + str(c) + '\n')
    f.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))