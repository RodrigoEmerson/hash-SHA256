import hashlib

arquivo = 'exemplo.txt'

# Cria um objeto hash SHA-256
hash_obj = hashlib.sha256()

# Abre o arquivo em modo binário
with open(arquivo, 'rb') as f:
    # Lê o arquivo em blocos de 4KB para evitar problemas de memória com arquivos grandes
    while True:
        bloco = f.read(4096)
        if not bloco:
            break
        # Atualiza o objeto hash com o bloco lido
        hash_obj.update(bloco)

# Gera a hash SHA-256 em formato hexadecimal
hash_hex = hash_obj.hexdigest()

print("Hash SHA-256 do arquivo:")
print(hash_hex)


