import unittest
from google.cloud import storage
from storage_handler import StorageHandler


client = storage.Client()
bucket = client.create_bucket("test_bucket")


class TestStorageHandler(unittest.TestCase):

    
