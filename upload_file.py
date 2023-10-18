from google.cloud import storage

project_id = "legal-management-system-399510"
#TODO: FIX Cloud Functions
def list_buckets(project_id=project_id):
    """This function will list all buckets. """
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")
    
    
def create_new_bucket(project_id=project_id):
    """ Creates a Client object that allows the script to communicate 
        with Google Cloud Storage and perform operations on it (like 
        creating a bucket). """
    storage_client = storage.Client(project=project_id)

    # Creates a new bucket with a specified name
    name = input("Enter name of bucket: ")
    bucket = storage_client.create_bucket(name)
    
    # Prints a message indicating the bucket was successfully created.
    bucketName = bucket.name
    print(f"Bucket {bucketName} created.")


def upload_object_from_filename(fileLocation ):
    """Uploads a file from your computer as a blob object"""
    client = storage.Client(project=project_id)
    bucket_name = "my-first-test-bucket-146541"
    # Get a reference to the bucket you want to upload to
    bucket = client.bucket(f"{bucket_name}")

    # Create a new blob object
    fileName =  f"{fileLocation}"
    blob = bucket.blob(f"{fileName}")

    # Upload the file to the bucket
    # TODO: popup to select file from computer
    if blob.upload_from_filename(f"{fileName}"): # It works but still goes to else statement 
        print("File successfully uploaded to bucket.")
    else:
        print("Error uploading file to bucket.")

def download_object_from_bucket(blob_name, file_path):
    """Downloads a file from the cloud"""
    try:
        client = storage.Client(project=project_id)
        bucket_name = "my-first-test-bucket-146541"
        blob = bucket.blob(blob_name)
        with open(file_path, "wb") as f:
            storage_client.download_object_from_bucket(blob, f)
        pass
    except:    
        pass
    
# list_buckets()
# create_new_bucket()
# upload_object_from_filename()