# hash-SHA256

Este projeto implementa a geração de hash utilizando o algoritmo SHA-256 em Python. Ele permite calcular o hash SHA-256 de arquivos ou textos, garantindo integridade e segurança de dados.

## Descrição

O código fornece uma interface simples para calcular o hash SHA-256 de qualquer arquivo ou string. O SHA-256 é um algoritmo de hash criptográfico amplamente utilizado para verificar a integridade de dados e armazenar senhas de forma segura.

## Funcionalidades

- Calcular o hash SHA-256 de arquivos.
- Calcular o hash SHA-256 de strings/textos.
- Interface de linha de comando para facilitar o uso.
- Saída do hash em formato hexadecimal.

## Pré-requisitos

- Python 3.6 ou superior instalado.
- (Opcional) Git para clonar o repositório.

## Instalação

Clone este repositório ou faça o download dos arquivos:

```bash
git clone https://github.com/RodrigoEmerson/hash-SHA256.git
cd hash-SHA256
```

## Como Executar

Execute o script principal via terminal:

```bash
python sha256.py
```

Siga as instruções exibidas para informar o arquivo ou texto a ser processado.

## Exemplo de Uso

### Gerar hash de um arquivo

```bash
python sha256.py --file exemplo.txt
```

Saída esperada:
```
SHA-256: 9a0b6c... (hash hexadecimal)
```

### Gerar hash de uma string

```bash
python sha256.py --text "minha senha secreta"
```

Saída esperada:
```
SHA-256: 5e8848... (hash hexadecimal)
```

## Observações

- Certifique-se de que o arquivo informado existe e possui permissões de leitura.
- O algoritmo SHA-256 é unidirecional, ou seja, não é possível reverter o hash para obter o texto original.

## Autor

[Rodrigo](https://github.com/RodrigoEmerson)

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
