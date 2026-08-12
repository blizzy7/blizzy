value = "Abiola"
def reverse_string(value):
    rev = ""
    for val in range(len(value) -1, -1, -1):
        rev +=  value[val]
    return rev

print(reverse_string(value))