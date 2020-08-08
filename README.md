# SQS-Buffer
SQS Buffer for Dynamo DB

## What is a SQS Buffer?
SQS is Amazon's Queue Service. SQS can act as a buffer for DynamoDB by making a Queue of DynamoDB Table Writes. This reduces the load on Dynamo DB, and can help save costs.

Sample SQS Buffer Architecture:

<a href="https://ibb.co/d7KN7JC"><img src="https://i.ibb.co/0QJ0QV4/SQS-Buffer-1.png" alt="SQS-Buffer-1" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />

In this architecture, we see the SQS Queue acting as a buffer from the Web Server to the DynamoDB Table. This buffer helps reduce the load on the DynamoDB, and can increase performance and availability of your architecture.

Send.py is a python script for the webserver to write random data to the SQS Queue

Receive.py is a python script for the worker instances to run, allowing them to write SQS Data to the Dynamo DB Table
