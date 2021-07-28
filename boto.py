import boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='eng89madeline-boto3', CreateBucketConfiguration= {'LocationConstraint': 'eu-west-1'})

s3_client = boto3.client('s3')
s3.upload_file("images/bat.jpg", "eng89madeline-boto3", "bat.jpg")
s3.download_file("eng89madeline-boto3", "bat.jpg", "images/bat2.jpg")

s3.Bucket('eng89madeline-boto3').bucket.objects.all().delete()