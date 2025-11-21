# Verificador de Integridade de Arquivos (SHA-256) em Python
Este é um projeto desenvolvido para fins de estudo em **cibersegurança**, focado na validação de arquivos usando de hash criptográficos.

O objetivo é simular uma ferramenta real utilizada em ambientes de segurança, permitindo gerar e verificar assinaturas (hashes) para assegurar que um arquivo não foi modificado.

O sistema é executado inteiramente via **linha de comando (CLI)** e permite gerar hashes, verificar a integridade e manipular arquivos de teste.

## Tech Stack
[![My Skills](https://skillicons.dev/icons?i=python,linux)](https://skillicons.dev)
## Funcionalidades
O sistema permite ao usuário executar as seguintes ações via terminal:

- **Gerar hash SHA-256 (`generate`)**
    
   Cria automaticamente um arquivo `.sha256` contendo a assinatura digital do arquivo original.
- **Verificar integridade (`verify`)**

   Lê o hash salvo no arquivo `.sha256`, recalcula o hash atual do arquivo e compara os valores.
- **Detecção de adulteração**

   Caso o conteúdo do arquivo tenha sido alterado, a ferramenta alertará imediatamente.
- **Tratamento de erros**

    Mensagens claras para arquivos inexistentes ou hashes ausentes.

## Estrutura de Dados e Tecnologia
* `open()` e operações de leitura binária: manipulação segura de arquivos.
* `hashlib.sha256`: algoritmo de hash criptograficamente seguro.
* `sys.argv`: leitura de argumentos via CLI.

A escolha dessas ferramentas visa manter o projeto simples, portátil e seguro.

## Como Executar
Este é um projeto simples que não depende de bibliotecas externas.

**1. Clone o repositório:**
```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
```

**2. Execute a ferramenta:**

Escolha o comando de acordo com seu sistema operacional:

#### Linux / macOS

### 🔸 Gerar hash:
```bash
   python3 file_integrity_checker.py generate <nome_do_arquivo.txt>
```

### 🔸 Verificar hash:
```bash
   python3 file_integrity_checker.py verify <nome_do_arquivo.txt>
```
---

#### Windows
### 🔸 Gerar hash:
```bash
   python file_integrity_checker.py generate <nome_do_arquivo.txt>
```
### 🔸 Verificar hash:
```bash
   python file_integrity_checker.py verify <nome_do_arquivo.txt>
```

**3. O resultado será exibido no terminal informando a situação do arquivo.**

## Estrutura de Arquivos
O projeto segue uma estrutura simples e objetiva:

```bash
   📂 projeto/
   ├── file_integrity_checker.py      # Arquivo principal com toda a lógica
   ├── README.md                      # Documentação
   └── data/
    ├── arquivo_teste.txt
    └── arquivo_teste.txt.sha256
```