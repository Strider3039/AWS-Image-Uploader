# AWS-Image-Uploader

**Disclaimer:**
This project is a work in progress and may not be finished at the time of reading.

## Description
I am aiming to make an image upload service that allows users to upload images through a frontend portal which will travel through an AWS pipeline, to eventually reach the uploads database. 

This pipeline includes:

```
Frontend
   |
   | upload image
   v
S3 Bucket
   |
   | ObjectCreated event
   v
Lambda #1: Metadata Extractor
   |
   | send JSON message
   v
SQS Queue
   |
   | worker consumes messages
   v
Lambda #2 or EC2 Worker
   |
   | insert metadata
   v
PostgreSQL on RDS
```

## Purpose:
Something I have realized in my journey of programming is how useful of a tool AWS is. I just have not had many chances to learn and use it as a student and growing software engineer. Building the Image Uploader is a good opportunity for me to use many aws tools and familiarize myself with the platform.
