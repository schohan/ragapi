import os
import boto3
from botocore.exceptions import NoCredentialsError

class S3FileManager:
    """ Service to download files from a given S3 bucket. """

    def __init__(self, bucket_name, local_download_dir):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.local_download_dir = local_download_dir
        if not os.path.exists(self.local_download_dir):
            os.makedirs(self.local_download_dir)


    def download_files(self, file_types=None):
        """
        Fetches files of specific types (pdf, docx, etc.) from the S3 bucket and stores them locally.
        :param file_types: List of file extensions to fetch. Example: ['pdf', 'docx']
        """
        try:
            # List objects in the S3 bucket
            response = self.s3.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' not in response:
                print("No files found in the bucket.")
                return

            for obj in response['Contents']:
                file_name = obj['Key']
                file_ext = os.path.splitext(file_name)[1][1:].lower()

                # Check if the file type is one of the types we're looking for
                if file_types is None or file_ext in file_types:
                    self.download_file(file_name)
                    
        except NoCredentialsError:
            print("S3 credentials not available.")


    def download_file(self, file_name):
        """
        Download a single file from the S3 bucket.
        :param file_name: The key of the file to download.
        """
        local_file_path = os.path.join(self.local_download_dir, file_name)
        try:
            self.s3.download_file(self.bucket_name, file_name, local_file_path)
            print(f"Downloaded {file_name} to {local_file_path}")
        except Exception as e:
            print(f"Failed to download {file_name}: {e}")


# Usage
if __name__ == "__main__":
    bucket_name = "dev-ssc-ragapi"
    local_download_dir = "./local_download_dir"
    file_types = ['pdf', 'docx']
    
    s3_file_manager = S3FileManager(bucket_name, local_download_dir)
    s3_file_manager.download_files(file_types)