def to_bucket(filename, bucket, upload_name = None):
    '''script that uploads a file to an amazon s3 bucket
    Parameters:
    -------
    filename: string. The name of the file
    bucket: string The s3 bucket you are uploading the file to
    upload_name: (optional) string. a new name you want to give the uploaded file
    
    Returns:
    string that confirms process
    '''
    import boto3
    s3 = boto3.client('s3')
    if upload_name == None:
        upload_name = filename
    s3.upload_file(filename, bucket, upload_name)
    return(f'{filename} has been uploaded to {bucket} as {upload_name}')
