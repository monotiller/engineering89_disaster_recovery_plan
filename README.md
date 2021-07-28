# Disaster recovery plan
## CRUD
- Create
- Read
- Update
- Delete

![](images/image1.png)

Pre-requisites for this lesson:
- SSH into your EC2 in the same region
- AWS access and secret keys
- We’ll set up an AWS CLI (command line interface)
- Apply CRUD from using AWSCLI from our EC2 instance

## Creating an S3 bucket
- `aws s3 mb s3://nameofbucket`
    - mb stands for “make bucket”
- Upload a file: `aws s3 cp test.txt s3://nameofbucket`

And here it is:

![](images/image2.png)

- And to copy it back: `sudo aws s3 cp s3://nameofbucket/test.txt test.txt`
- And to remove it from s3: `aws s3 rm s3://nameofbucket/test.txt`

## Getting everything set up
Create a new EC2 instance and follow these steps:
### Installing Python 3.9 and the Latest pip Version on Linux
```console
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.9 #Latest version of python
```
Then open up your `.bashrc` file and enter in: `alias python=python3`

Then install pip
```console
sudo apt-get install python3-pip
```
### Installing awscli and boto3
```console
sudo pip3 install awscli
sudo pip3 install boto3
```
### Connecting to AWS
Run `aws configure` and follow the instructions
### Create a Bucket
```console
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket=bucket_name)
```
### Upload a File
```console
s3_client = boto3.client('s3')
s3_client.upload_file(file_name, bucket, object_name)
```
### Download a File
```console
s3 = boto3.client('s3')
s3.download_file(BUCKET_NAME, OBJECT_NAME, FILE_NAME)
```
### Delete a File
```console
s3 = boto3.resource("s3")
obj = s3.Object(BUCKET_NAME, OBJECT_NAME)
obj.delete()
```

### Delete EVERYTHING in the bucket
```console
s3.Bucket(BUCKET_NAME).bucket.objects.all().delete()
```

### Delete a Bucket
```console
client = boto3.client('s3')
client.delete_bucket(Bucket=BUCKET_NAME)
```