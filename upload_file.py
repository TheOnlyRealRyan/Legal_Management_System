from google.cloud import storage
import tkinter.messagebox

# Intitialise Cloud Environment
project_id = "legal-management-system-399510"
client = storage.Client(project=project_id)


def list_buckets():
    """This function will list all buckets. """
    # client = storage.Client(project=project_id)
    buckets = client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")
    
    
def create_new_bucket():
    """ Creates a Client object that allows the script to communicate 
        with Google Cloud Storage and perform operations on it (like 
        creating a bucket). """
    # client = storage.Client(project=project_id)

    # Creates a new bucket with a specified name
    name = input("Enter name of bucket: ")
    bucket = client.create_bucket(name)
    
    # Prints a message indicating the bucket was successfully created.
    bucketName = bucket.name
    print(f"Bucket {bucketName} created.")


def upload_object_from_filename(name, fileLocation):
    """Uploads a file from your computer as a blob object"""
    try:        
        # client = storage.Client(project=project_id)
        bucket_name = "case-file-upload-bucket"
        bucket = client.bucket(f"{bucket_name}")

        # Create a new blob object
        blob = bucket.blob(name)

        # Upload the file to the bucket
        blob.upload_from_filename(fileLocation)
        print("Successful upload")
    except Exception as e:
        print(e)
        
        
def download_object_from_bucket(blob_name):
    """Downloads a file from the cloud. Get blob_name from the cloud file name"""
    try:
        # This downloads to the folder that the app is located in
        bucket_name = "case-file-upload-bucket"
        bucket = client.bucket(f"{bucket_name}")
        blob = bucket.blob(blob_name)
        with open(blob_name, "wb") as f:
            client.download_blob_to_file(blob, f)
        tkinter.messagebox.showinfo("Success",  "Succesfully downloaded")
        print("Successful Download")
    except Exception as e:    
        print(e)
        tkinter.messagebox.showinfo("Failed",  "Failed downloaded")
    
# list_buckets()
# create_new_bucket()
# upload_object_from_filename()