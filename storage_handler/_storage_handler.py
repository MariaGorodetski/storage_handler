from google.cloud import storage
import os


class StorageHandler():
    
    def __init__(self, bucket_name):
        client = storage.Client()
        self.bucket = client.get_bucket(bucket_name)

    def upload_object(self, object_name, new_object_name):
        if new_object_name is not None:
            object = self.bucket.blob(new_object_name)
        else:
            object_name_tail = os.path.split(object_name)[1]
            object = self.bucket.blob(object_name_tail)
        with open(object_name, 'rb') as file_name:
            object.upload_from_file(file_name)
    
    def download_object(self, object_name, new_object_name):
        object = self.bucket.blob(object_name)
        if new_object_name is not None:
            object.download_to_filename(new_object_name)
        else:
            object.download_to_filename(object_name)

    def objects_list(self):
        objects = self.bucket.list_blobs()
        return objects
