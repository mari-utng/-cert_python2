from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa un nombre: ")
try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->', cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))