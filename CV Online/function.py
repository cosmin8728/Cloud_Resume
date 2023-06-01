import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-table')

def lambda_handler(event, context):


    response = table.get_item(Key={
       'record_id':'VisitorCount'
    })

    visitor_count = response['Item']['visitor_count']
    visitor_count = visitor_count + 1
    print(visitor_count)

 

    response = table.put_item(Item={
            'record_id':'VisitorCount',
            'visitor_count': visitor_count
    })

    response = {
      'statusCode': 200,
      'body': visitor_count,
      'headers' : {
        'Access-Control-Allow-Origin': '*'
      }

            }

    return response