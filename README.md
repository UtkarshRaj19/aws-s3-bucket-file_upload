# aws-s3-bucket-file_upload
Here is a function in python to upload files/images/videos directly to your Amazon S3 Bucket and create a URL to access it

Before you proceed there are certain prerequisites for it

# Step 1: Setup a AWS S3 Bucket if not already
Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/

# Step 2: Find region and credentials of your S3 Bucket
You can find the region in the url, when you preview the desired bucket https://s3.console.aws.amazon.com/s3/buckets/vprefgvb/?region=as-singapore-2 (In this case: as-singapore-2)

Copy access and secret from https://console.aws.amazon.com/iam/home?#/security_credential (Security Credentials -> Access keys (access key ID and secret access key) -> Create New Access Key -> Show Access Key)

# Step 4: Now we come to our Python File and set it up

We will use python3 and boto3 

pip install boto3 (if not already)

# Step 5: Imports in your python file

import boto3
import os (to set environment variables)
import secrets (to give a unique name to the file uploaded in order to prevent overwriting)

# Step 6: Set environment variables

os.environ['AWS_ACCESS_KEY_ID'] = '<YOUR_AWS_ACCESS_KEY>'
os.environ['AWS_SECRET_ACCESS_KEY'] = '<YOUR_AWS_SECRET_KEY>'

This will set <AWS_ACCESS_KEY_ID> and <AWS_SECRET_ACCESS_KEY> as global variables that can be used anywhere

# Step 7: Setup boto3 client

s3 = boto3.client('s3',
                    aws_access_key_id="<YOUR_AWS_ACCESS_KEY>",
                    aws_secret_access_key= "<YOUR_AWS_SECRET_KEY>")

This will initiate a connection to your <AWS S3 Bucket> using the credentials

# Step 8: Upload File to the Program

file = request.FILES.get("<File Name>")

hex = secrets.token_hex(16)  (This will create a unique 32 characters string for the filename)

# Step 9: Get the content type for the file uploaded

This step is necessary as it will help you open or view your file in the browser.
If you miss this step your fill will download rather than opening in the browser.

def s3_content_type(file):
    try:
        result = os.path.splitext(file.name)
        print('Extension:', result[1])
        Extension = result[1].replace(".","")
        switcher = {
        'png': "image/png",
        'gif': "image/gif",
        'html': "text/html",
        'htmls': "text/html",
        'htm': "text/html",
        'jpg': "image/jpeg",
        'jpeg': "image/jpeg",
        'jfif': "image/jpeg",
        'pdf': "application/pdf",
        'webp': "image/webp"
        }
        return switcher.get(Extension, "nothing")
    except Exception as e:
        print(e)

You can modify the above function according to your needs and type of file uploaded
You can reference file types here - https://www.ibm.com/docs/en/aspera-on-cloud?topic=SS5W4X/dita/content/aws_s3_content_types.htm

<NOTE :> The above function will recieve the file and will return the content type of it to be used further in the program

# Step 10: Final Program

filee = request.FILES.get("<File Name>")
content_type = s3_content_type(filee)  (Passing the file to the function stated above)
hex = secrets.token_hex(16)
directory = '<YOUR FILE PATH>/{}{}'.format(hex,filee) # Path where file is to be saved
s3.put_object(Bucket='<YOUR_BUCKET_NAME>', Key=directory, Body=filee,ContentType=content_type)
path = "https://<YOUR_BUCKET_NAME>.s3.amazonaws.com/"+directory

# Step 11: Open your uploaded file in the browser using the URL generated in the path variable in the above step

path = "https://<YOUR_BUCKET_NAME>.s3.amazonaws.com/"+directory



