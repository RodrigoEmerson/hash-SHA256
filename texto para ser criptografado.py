import hashlib

texto = "Este é um exemplo de texto para ser criptografado."

# Cria um objeto hash SHA-256
hash_obj = hashlib.sha256()

# Converte o texto em bytes e atualiza o objeto hash
hash_obj.update(texto.encode('utf-8'))

# Gera a hash SHA-256 em formato hexadecimal
hash_hex = hash_obj.hexdigest()

print("Hash SHA-256 do texto:")
print(hash_hex)
print(len(hash_hex))
