import argparse
from _storage_handler import Storage_handler


def object_upload():
    parser = argparse.ArgumentParser(
        description='Uploading a new object to an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket', type=str,
        help='Bucket name')
    parser.add_argument(
        '--object', dest='object', type=str,
        help='The name of the object being uploaded')
    parser.add_argument(
        '--new_object', dest='new_object', type=str,
        help='The new name of the uploaded object', default=None)
    args = parser.parse_args()
    bucket = Storage_handler(args.bucket)
    bucket.upload_object(args.object, args.new_object)


def object_download():
    parser = argparse.ArgumentParser(
        description='Downloading an object from an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket', type=str,
        help='Bucket name')
    parser.add_argument(
        '--object', dest='object', type=str,
        help='The name of the object being downloaded')
    parser.add_argument(
        '--new_object', dest='new_object', type=str,
        help='The new name of the downloaded object', default=None)
    args = parser.parse_args()
    bucket = Storage_handler(args.bucket)
    bucket.download_object(args.object, args.new_object)

    
def list_objects():
    parser = argparse.ArgumentParser(
        description='List of objects from an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket', type=str,
        help='Bucket name')
    args = parser.parse_args()
    bucket = Storage_handler(args.bucket)
    bucket.objects_list()
