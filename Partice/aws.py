import boto3

# Initialize a session using your configured credentials
session = boto3.Session()

# Create an S3 client
s3_client = session.client('s3')

try:
    # Test connection by listing all S3 buckets
    response = s3_client.list_buckets()

    # If no exception was raised, print success message
    print("Successfully connected to AWS!")
    print("List of S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

except Exception as e:
    print("Failed to connect to AWS:", str(e))