import boto3
import json
import pandas as pd


def receiveMessage():
    sqs = boto3.client("sqs")

    queue_url = "https://sqs.us-east-1.amazonaws.com/306784070391/test"

    # Receive SQS Message
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["SentTimestamp"],
        MaxNumberOfMessages=1,
        MessageAttributeNames=["All"],
        VisibilityTimeout=0,
        WaitTimeSeconds=0,
    )
    print(response)
    key = "Messages"
    if key in response.keys():

        message = response["Messages"][0]

        receipt_handle = message["ReceiptHandle"]
        message = json.dumps(message)
        # Delete received message from queue
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)

        # print('Received and deleted message: %s' % message)

        column1 = "MessageAttributes__|"
        column2 = "MessageAttributes__|__StringValue"
        df = pd.read_json(message)
        # print("-------------------")
        # print(df)
        # print("--------------------")
        author = df["MessageAttributes"]["Author"]
        author = author["StringValue"]
        title = df["MessageAttributes"]["Title"]
        title = title["StringValue"]
        weeks = df["MessageAttributes"]["WeeksOn"]
        weeks = weeks["StringValue"]
        # print("-------------------")
        # print(author)
        # print(title)
        # print(weeks)
        # print("--------------------")
        dynamodb = boto3.resource("dynamodb")

        table = dynamodb.Table("test")

        table.put_item(
            Item={
                "title": title,
                "author": author,
                "weeks": weeks,
                "SQSBookAttributes": message,
            }
        )
    else:
        print("no messages")


import time

while True:
    receiveMessage()
    time.sleep(5)

<<<<<<< HEAD
# receiveMessage()
=======
#receiveMessage()
>>>>>>> de1cbe3799fe1ac5a26a9f4f18715c8fd34c5180
