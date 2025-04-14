from cryptography.fernet import Fernet
import pandas as pd
import base64

senha = input("Digite uma senha: ").encode()
chave = base64.urlsafe_b64encode(senha.ljust(32, b'0'))
fernet = Fernet(chave)

df = pd.DataFrame({"Nome": ["Ana", "Lucas"], "Nota": [8.5, 7.3]})
dados_serializados = df.to_csv(index=False).encode()

criptografado = fernet.encrypt(dados_serializados)
print("\nDados criptografados:")
print(criptografado)

descriptografado = fernet.decrypt(criptografado).decode()
print("\nDados recuperados:")
print(descriptografado)