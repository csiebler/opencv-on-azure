from azure.storage.blob import BlockBlobService
import os

account_name = os.environ['ACCOUNT_NAME']
sas_token = os.environ['SAS_TOKEN']
download_container_name = os.environ['DOWNLOAD_CONTAINER_NAME']
download_file_name = os.environ['DOWNLOAD_FILE_NAME']

blob_service = BlockBlobService(account_name=account_name, sas_token=sas_token)
blob_service.get_blob_to_path(download_container_name, download_file_name, 'temp.mp4')