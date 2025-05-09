from google.cloud import storage

class GoogleStorageClient:
    def __init__(self, credentials_path):
        """Inicializa o cliente do Google Cloud Storage"""
        self.client = storage.Client().from_service_account_json(credentials_path)

    def list_files(self, bucket_name, prefix=None):
        """Lista todos os arquivos no bucket com o prefixo opcional"""
        bucket = self.client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)

        return [blob.name for blob in blobs if not blob.name.endswith('/')]

    def download_file(self, bucket_name, file_name):
        """Baixa um arquivo do Google Cloud Storage"""
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        return blob.download_as_bytes()