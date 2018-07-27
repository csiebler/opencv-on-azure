from azure.storage.blob import BlockBlobService
import os

account_name = os.environ['ACCOUNT_NAME']
sas_token = os.environ['SAS_TOKEN']
upload_container_name = os.environ['UPLOAD_CONTAINER_NAME']
upload_file_name = os.environ['UPLOAD_FILE_NAME']

blob_service = BlockBlobService(account_name=account_name, sas_token=sas_token)
blob_service.create_blob_from_path(upload_container_name, upload_file_name, upload_file_name)
