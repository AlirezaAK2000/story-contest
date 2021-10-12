from django.conf import settings
import boto3


s3_resource = boto3.resource(
    's3',
    endpoint_url = settings.ARVAN_STORAGE_ENDPOINT_URL,
    aws_access_key_id = settings.ARVAN_STORAGE_ACCESS_KEY_ID,
    aws_secret_access_key = settings.ARVAN_STORAGE_SECRET_ACCESS_KEY
)

s3_client = boto3.client(
    's3',
    endpoint_url = settings.ARVAN_STORAGE_ENDPOINT_URL,
    aws_access_key_id = settings.ARVAN_STORAGE_ACCESS_KEY_ID,
    aws_secret_access_key = settings.ARVAN_STORAGE_SECRET_ACCESS_KEY
)

bucket = s3_resource.Bucket(settings.ARVAN_STORAGE_BUCKET_NAME)
