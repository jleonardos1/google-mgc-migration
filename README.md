# Guia de Uso do Script de Migração de Armazenamento

Este script realiza a migração de arquivos de um bucket no Google Cloud Storage para um bucket no Magalu Cloud.

## Instalação de Dependências

Certifique-se de ter o Python instalado em sua máquina. Em seguida, instale as dependências necessárias executando:

```bash
pip install -r requirements.txt
```

## Como Executar o Script

Para executar o script, utilize o seguinte comando:

```bash
python migrate_storage.py \
    --google-bucket GOOGLE_BUCKET \
    --magalu-bucket MAGALU_BUCKET \
    --magalu-access-key MAGALU_ACCESS_KEY \
    --magalu-secret-key MAGALU_SECRET_KEY \
    --magalu-endpoint MAGALU_ENDPOINT \
    --google-credentials GOOGLE_CREDENTIALS \
    [--prefix PREFIX] \
    [--dry-run]
```

### Parâmetros

- `--google-bucket`: Nome do bucket no Google Cloud Storage.
- `--magalu-bucket`: Nome do bucket no Magalu Cloud.
- `--magalu-access-key`: Chave de acesso para o Magalu Cloud.
- `--magalu-secret-key`: Chave secreta para o Magalu Cloud.
- `--magalu-endpoint`: Endpoint do Magalu Cloud (opcional).
- `--google-credentials`: Caminho para o arquivo de credenciais do Google Cloud.
- `--prefix`: Prefixo para filtrar os arquivos a serem migrados (opcional).
- `--dry-run`: Simula a migração sem realizar uploads (opcional).

## Exemplo de Execução

```bash
python migrate_google_to_mgc.py \
    --google-bucket meu-bucket-google \
    --magalu-bucket meu-bucket-magalu \
    --magalu-access-key minha-chave-de-acesso \
    --magalu-secret-key minha-chave-secreta \
    --magalu-endpoint https://endpoint.magalu.com \
    --google-credentials /caminho/para/credenciais.json \
    --prefix imagens/ \
    --dry-run
```

## Observações

- Certifique-se de que as credenciais fornecidas possuem permissões adequadas para acessar os buckets.
- O parâmetro `--dry-run` é útil para verificar quais arquivos seriam migrados sem realizar alterações.
```