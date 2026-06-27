
# Disclaimer: This is purely a copy of the lambda function used in the aws pipeline for code review purposes.

import json
import urllib
import boto3

def lambda_handler(event, context):
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        decodedKey = urllib.parse.unquote_plus(key, encoding='utf-8')

        boto3Client = boto3.client('s3')
        obj = boto3Client.head_object(Bucket=bucket, Key=decodedKey)

        metadata = {
            'bucket': bucket,
            'key': decodedKey,
            'fileSize': obj['ContentLength'],
            'lastModified': obj['LastModified'].strftime("%Y-%m-%d %H:%M:%S"),
            'contentType': obj['ContentType'],
            'eTag': obj['ETag']
        }

        print(metadata)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
