from google.cloud import storage

project_id = "legal-management-system-399510"

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
    print("Bucket {} created.".format(bucket.name))


def upload_object_from_filename(project_id=project_id):
    """Uploads a file from your computer as a blob object"""
    client = storage.Client(project=project_id)

    # Get a reference to the bucket you want to upload to
    bucket = client.bucket("my-first-test-bucket-146541")

    # Create a new blob object
    blob = bucket.blob("file2.txt")

    # Upload the file to the bucket
    # TODO: popup to select file from computer
    if blob.upload_from_filename("./files_to_upload/file2.txt"): # It works but still goes to else statement 
        print("File successfully uploaded to bucket.")
    else:
        print("Error uploading file to bucket.")

def download_object(project_id=project_id):
    """Downloads a file from the cloud"""
    pass
    
list_buckets()
# create_new_bucket()
upload_object_from_filename()