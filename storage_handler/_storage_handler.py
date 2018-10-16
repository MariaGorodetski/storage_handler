from google.cloud import storage


def upload_object(bucket_name, object_name, new_object_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    if new_object_name is not None:
        object = bucket.blob(new_object_name)
    object = bucket.blob(object_name)
    object.upload_from_file(object_name)

def download_object(bucket_name, object_name, new_object_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    object = bucket.blob(object_name)
    if new_object_name is not None:
        object.download_to_filename(new_object_name)
    else:
        object.download_to_filename(object_name)


def objects_list(bucket_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    objects = bucket.list_blobs()

    for object in objects:
        print object.name