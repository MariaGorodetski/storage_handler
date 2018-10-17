import unittest
from google.cloud import storage
import os
from storage_handler import StorageHandler


class TestStorageHandler(unittest.TestCase):

    def setUp(self):
        bucket_name = "daytwo-test-bucket"
        client = storage.Client()
        self.new_bucket = client.create_bucket(bucket_name)
        self.path = './test/sample_files'
        self.bucket = StorageHandler(bucket_name)
        self.bucket_objects = []

    def tearDown(self):
        for object in self.bucket_objects:
            self.new_bucket.blob(object).delete()
        self.new_bucket.delete()

    def test_all(self):
        object_names = os.listdir(self.path)
        objects_in_dir = os.listdir('./')

        new_objects_names = []
        for object in object_names:
            self.bucket.upload_object(self.path+'/' + object, None)
            self.bucket.upload_object(self.path+'/' + object, 'new_' + object)
            new_objects_names += ['new_' + object]
        object_names = sorted(object_names + new_objects_names)
        bucket_list = self.bucket.objects_list()
        self.bucket_objects = [str(o.name) for o in bucket_list]
        objects_number = len(object_names)
        for i in range(objects_number):
            self.assertEquals(object_names[i], self.bucket_objects[i])

        new_objects_names = []
        for object in object_names:
            self.bucket.download_object(object, None)
            self.bucket.download_object(object, 'down_' + object)
            new_objects_names += ['down_'+object]
        sample_files_objects = object_names + new_objects_names
        object_names = sorted(sample_files_objects + objects_in_dir)
        objects_in_dir = sorted(os.listdir('./'))
        objects_number = len(object_names)
        for i in range(objects_number):
            self.assertEqual(object_names[i], objects_in_dir[i])

        for object in sample_files_objects:
            os.remove(object)

    if __name__ == '__main__':
        unittest.main()
