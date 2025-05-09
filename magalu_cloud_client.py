import boto3
from botocore.exceptions import ClientError

class MagaluCloudClient:
    def __init__(self, access_key, secret_key, endpoint):
        """Inicializa o cliente do Magalu Cloud usando boto3"""
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint
        )

    def upload_file(self, bucket_name, file_name, file_content):
        """Envia um arquivo para o Magalu Cloud"""
        try:
            self.client.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=file_content
            )
        except ClientError as e:
            raise Exception(f"Falha no upload: {e}")