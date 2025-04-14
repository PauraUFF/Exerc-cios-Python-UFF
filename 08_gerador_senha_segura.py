import random
import string

tamanho = int(input("Tamanho da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=tamanho))

print(f"Senha gerada: {senha}")