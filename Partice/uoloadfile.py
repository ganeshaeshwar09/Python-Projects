import boto3
from botocore.exceptions import NoCredentialsError
import os


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        # Set the Content-Type and make the file public
        s3.upload_file(
            local_file, bucket, s3_file,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': 'image/jpeg'  # Set the appropriate MIME type
            }
        )
        print(f"Upload Successful: {local_file} to {bucket}/{s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def generate_s3_url(bucket, s3_file):
    return f"https://{bucket}.s3.amazonaws.com/{s3_file}"


if __name__ == "__main__":
    # User input for file path and bucket name
    local_file = input("Enter the path to the file you want to upload: ")
    bucket_name = input("Enter the name of the S3 bucket: ")

    # Get the file name to use in S3
    s3_file_name = os.path.basename(local_file)

    # Upload the file
    if upload_to_aws(local_file, bucket_name, s3_file_name):
        # Generate and print the S3 URL
        url = generate_s3_url(bucket_name, s3_file_name)
        print(f"File is publicly accessible at: {url}")
