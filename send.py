import boto3
from random_words import RandomWords
from random_words import RandomNicknames
import random

# Create random word client
def sendMessage():
    r = RandomWords()
    rn = RandomNicknames()
    # Create SQS client
    sqs = boto3.client("sqs")

    queue_url = "https://sqs.us-east-1.amazonaws.com/306784070391/test"

    # Generate Random Title
    title = r.random_word()

    # Generate Random Author
    author = rn.random_nick(letter="r", gender="m")

    # Generate Random Number of Weeks
    weeks = random.randint(0, 10)

    weeksFinal = str(weeks)
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            "Title": {"DataType": "String", "StringValue": title},
            "Author": {"DataType": "String", "StringValue": author},
            "WeeksOn": {"DataType": "Number", "StringValue": weeksFinal},
        },
        MessageBody=("Information about current NY Times fiction bestseller."),
    )

    print(response["MessageId"])
    return response["MessageId"]
