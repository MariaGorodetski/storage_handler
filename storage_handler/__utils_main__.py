import argparse
from _storage_handler import *


def object_upload():
    parser = argparse.ArgumentParser(
        description='Uploading a new object to an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket_name', type=str,
        help='Bucket name')
    parser.add_argument(
        '--object', dest='object_name', type=str,
        help='The name of the object being uploaded')
    parser.add_argument(
        '--new_object', dest='new_object', type=str,
        help='The new name of the uploaded object', default=None)
    args = parser.parse_args()
    upload_object(args.bucket, args.object, args.new_object)

def object_download():
    parser = argparse.ArgumentParser(
        description='Downloading an object from an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket_name', type=str,
        help='Bucket name')
    parser.add_argument(
        '--object', dest='object_name', type=str,
        help='The name of the object being downloaded')
    parser.add_argument(
        '--new_object', dest='new_object', type=str,
        help='The new name of the downloaded object', default=None)
    args = parser.parse_args()
    download_object(args.bucket, args.object, args.new_object)

def list_objects():
    parser = argparse.ArgumentParser(
        description='List of objects from an existing bucket')
    parser.add_argument(
        '--bucket', dest='bucket_name', type=str,
        help='Bucket name')
    args = parser.parse_args()
    objects_list(args.bucket)