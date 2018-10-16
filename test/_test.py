import unittest
from google.cloud import storage
import os
from storage_handler import StorageHandler

client = storage.Client()
bucket = client.create_bucket('daytwo-test-bucket')
path = "/sample_files/"

object_names = []
for f in os.listdir(path):
    object_names += f
object_names = sorted(object_names)


class TestStorageHandler(unittest.TestCase):

    def test_upload_object():
        for object in object_names:
            bucket.upload_object(path+object, None)
            bucket.upload_object(path+object, "new_"+object)
            object_names += ["new_"+object]
        object_names = sorted(object_names)
        bucket_list = bucket.objects_list()
        objects_number = len(bucket_list)
        for i in range(objects_number):
            assertEquals(object_names[i], bucket_list[i].name)
            assertNotEquals(object_names[i], bucket_list[i].name.upper())
            assertNotEquals(object_names[i], bucket_list[i].name.lower())
