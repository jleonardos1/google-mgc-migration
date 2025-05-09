import argparse

from botocore.exceptions import ClientError

from Logger import Logger
from google_storage_client import GoogleStorageClient
from magalu_cloud_client import MagaluCloudClient
from storage_migrator import StorageMigrator

def configure_parser():
        parser = argparse.ArgumentParser(description="Migra arquivos do Google Storage para Magalu Cloud")
        parser.add_argument("--google-bucket", required=True, help="Bucket no Google Cloud Storage")
        parser.add_argument("--magalu-bucket", required=True, help="Bucket no Magalu Cloud")
        parser.add_argument("--prefix", help="Prefixo para filtrar arquivos")
        parser.add_argument("--google-credentials", help="Credenciais do Google Cloud")
        parser.add_argument("--magalu-access-key", required=True, help="Acesso ao Magalu Cloud")
        parser.add_argument("--magalu-secret-key", required=True, help="Chave secreta do Magalu Cloud")
        parser.add_argument("--magalu-endpoint", help="Endpoint do Magalu Cloud")
        parser.add_argument("--dry-run", action="store_true", help="Simulação sem uploads")
        return parser

def initialize_google_storage(google_credentials, google_bucket):
    google_client = GoogleStorageClient(google_credentials)

    if not google_client.client.lookup_bucket(google_bucket):
        Logger.error("Bucket não encontrado.")
        exit(1)

    Logger.info("Conexão com o Google Cloud Storage estabelecida com sucesso.")

    return google_client

def initialize_mgc(magalu_access_key, magalu_secret_key, magalu_endpoint):
    magalu_client = MagaluCloudClient(
        magalu_access_key,
        magalu_secret_key,
        magalu_endpoint
    )

    try:
        magalu_client.client.list_buckets()
        Logger.info("Conexão com o Magalu Cloud estabelecida com sucesso.")
    except ClientError as e:
        Logger.error(f"Falha na conexão com o Magalu Cloud: {e}")
        exit(1)

    return magalu_client

if __name__ == "__main__":
    args = configure_parser().parse_args()

    try:
        google_client = initialize_google_storage(args.google_credentials, args.google_bucket)
        magalu_client = initialize_mgc(args.magalu_access_key, args.magalu_secret_key, args.magalu_endpoint)

        try:
            magalu_client.client.list_buckets()
            Logger.info("Conexão com o Magalu Cloud estabelecida com sucesso.")
        except ClientError as e:
            Logger.error(f"Falha na conexão com o Magalu Cloud: {e}")
            exit(1)

        StorageMigrator(google_client, magalu_client).migrate(
            args.google_bucket,
            args.magalu_bucket,
            args.prefix,
            args.dry_run
        )
    except Exception as e:
        Logger.error(f"Erro na migração: {str(e)}")
        exit(1)
