# Instalar dependências
pip install -r requirements.txt

# Executar o script
python migrate_google_to_mgc.py \
--source-bucket GOOGLE_BUCKET \
--target-bucket MAGALU_BUCKET \
--magalu-access-key MAGALU_ACCESS_KEY \
--magalu-secret-key MAGALU_SECRET_KEY \
--magalu-endpoint MAGALU_ENDPOINT \
--google-credentials GOOGLE_CREDENTIALS \
[--dry-run] 

