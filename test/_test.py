import unittest
from google.cloud import storage
import os
from storage_handler import StorageHandler


bucket_name = "daytwo-test-bucket"
client = storage.Client()
client.create_bucket(bucket_name)
path = './test/sample_files'
bucket = StorageHandler(bucket_name)


class TestStorageHandler(unittest.TestCase):

    def test_all(self):
        object_names = sorted(os.listdir(path))
        objects_in_dir = os.listdir('./')
        new_objects_names = []
        for object in object_names:
            bucket.upload_object(path+'/'+object, None)
            bucket.upload_object(path+'/'+object, 'new_'+object)
            new_objects_names += ['new_'+object]
        object_names = sorted(object_names+new_objects_names)
        bucket_list = bucket.objects_list()
        bucket_objects = [str(o.name) for o in bucket_list]
        objects_number = len(object_names)
        print objects_in_dir
        for i in range(objects_number):
            self.assertEquals(object_names[i], bucket_objects[i])
        new_objects_names = []
        for object in object_names:
            bucket.download_object(object, None)
            bucket.download_object(object, 'down_'+object)
            new_objects_names += ['down_'+object]
        sample_files_objects = object_names+new_objects_names
        object_names = sorted(sample_files_objects+objects_in_dir)
        objects_in_dir = sorted(os.listdir('./'))
        objects_number = len(object_names)
        for i in range(objects_number):
            self.assertEqual(object_names[i], objects_in_dir[i])
        for object in sample_files_objects:
            os.remove(object)
