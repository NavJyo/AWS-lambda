#A script to read environmnet variables 
import json
import os

def lambda_handler(event, context):
    
    print("IN")
    print(os.getenv("Name")) 
    print(event) 
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
