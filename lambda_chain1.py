import json
import boto3 
client = boto3.client('lambda') 


def lambda_handler(event, context):
    # TODO implement
    message = {"message" : "Hello! from lambda1"} 
    response = client.invoke(FunctionName='arn:aws:lambda:ap-northeast-1:077927045215:function:lambda_lab2_chain2',
    InvocationType = 'RequestResponse',
    Payload = json.dumps(message) 
    )
    print(response) 
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
