import os
import hashlib
from Crypto.Util import number

# 1. Establecer g=2 y el número primo p
g = 2
p = number.getPrime(256)  # Genera un número primo de 256 bits

# 2. Generar las llaves privadas de Alice (a) y Bob (b)
a = int.from_bytes(os.urandom(32), byteorder='big')  # Genera un número aleatorio de 256 bits
b = int.from_bytes(os.urandom(32), byteorder='big')  # Genera un número aleatorio de 256 bits

# 3. Simular el intercambio de números entre Alice y Bob
A = pow(g, a, p)
B = pow(g, b, p)

# 4. Calcular la llave secreta "s" y verificar que sean iguales mediante el uso de la función hash SHA-256
s_Alice = pow(B, a, p)
s_Bob = pow(A, b, p)

# Verificar que las llaves secretas son iguales
assert s_Alice == s_Bob

# Calcular el hash SHA-256 de la llave secreta
hash_s = hashlib.sha256(s_Alice.to_bytes(32, byteorder='big')).hexdigest()

print(f"La llave secreta es: {hash_s}")
