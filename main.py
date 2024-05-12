import random
from werkzeug.security import generate_password_hash


minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
num = "0123456789"
simbolos = "!@#$%^&*()_+=-,./"

base = minus + mayus + num +simbolos
lngitud = 12

muestra = random.sample(base,lngitud)
password = "".join(muestra)
password_Encryp = generate_password_hash(password)
print("{} => {} " .format(password,password_Encryp))



