import json
import os
import psycopg2

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_PORT = os.environ.get("DB_PORT", "5432")

def lambda_handler(event, context):
    print("Lambda started")
    print(json.dumps(event))

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    print("Connected to database")

    try:
        with conn:
            with conn.cursor() as cur:
                for record in event["Records"]:
                    print("Processing record")

                    metadata = json.loads(record["body"])
                    print(metadata)

                    cur.execute(
                        """
                        INSERT INTO image_metadata (
                            bucket, s3_key, file_size, content_type, last_modified, etag
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (
                            metadata["bucket"],
                            metadata["key"],
                            metadata["fileSize"],
                            metadata["contentType"],
                            metadata["lastModified"],
                            metadata["eTag"]
                        )
                    )

                    print("Inserted row")

        print("Done")

        return {
            "statusCode": 200,
            "body": json.dumps("Inserted metadata")
        }

    finally:
        conn.close()

    
