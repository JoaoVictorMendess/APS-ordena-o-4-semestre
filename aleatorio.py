import random

def rolar_dado():
    return random.randint(1, 6)

resultado = rolar_dado()

print(f"O dado rolou e o resultado foi: {resultado}")
