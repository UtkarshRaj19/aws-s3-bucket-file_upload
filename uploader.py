import boto3
import os
import secrets

os.environ['AWS_ACCESS_KEY_ID'] = '<YOUR_AWS_ACCESS_KEY>'
os.environ['AWS_SECRET_ACCESS_KEY'] = '<YOUR_AWS_SECRET_KEY>'

s3 = boto3.client('s3',
                    aws_access_key_id="<YOUR_AWS_ACCESS_KEY>",
                    aws_secret_access_key= "<YOUR_AWS_SECRET_KEY>")

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

def S3FileUploader_f(request):
    try:
        # Modify the below command to recieve file as per your requirements
        filee = request.FILES.get("File")
        
        content_type = s3_content_type(filee)
        hex = secrets.token_hex(16)
        directory = '<YOUR_PATH>/{}{}'.format(hex,filee)
        # The below command puts the file in your bucket at the 
        s3.put_object(Bucket='<YOUR_BUCKET_NAME>', Key=directory, Body=filee,ContentType=content_type)
        path = "https://<YOUR_BUCKET_NAME>.s3.amazonaws.com/"+directory
    except:
        return None