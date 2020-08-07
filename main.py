import boto3
from random_word import RandomWords
import random

#Create random word client
r = RandomWords()

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/306784070391/test'

#Generate Random Title
title = r.get_random_word(hasDictionaryDef="true")

#Generate Random Author
author = r.get_random_word()

#Generate Random Number of Weeks 
weeks = random.randint(0,10)

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': title
        },
        'Author': {
            'DataType': 'String',
            'StringValue': author
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': weeks
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller.'
    )
)

print(response['MessageId'])