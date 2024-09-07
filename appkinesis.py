import boto3
import base64
import json

def lambda_handler(event, context):
    session = boto3.Session(
    aws_access_key_id='your access key' ,
    aws_secret_access_key= 'your secret key',
    region_name='your aws region')

    dynamodb =  session.client('dynamodb') 
    dynamodbres = session.resource('dynamodb')
    table_name = 'capstone3'  
    isexisits = dynamodb.list_tables()['TableNames']
    
    print(f"Table name: {table_name}")
    if table_name in isexisits:
            table_data = dynamodbres.Table(table_name)
            for record in event['Records']:
                payload = base64.b64decode(record['kinesis']['data'])
                data = json.loads(payload)
                
                print(f"Data to put: {data}")

                item = {
                        "time": data["time"],
                        "iteam_id" : data["iteam_id"],
                        "iteam_name":data["iteam_name"],
                        "click_count":data["click_count"]
                    }

                try:
                    response = table_data.put_item(Item=item)
                    print(f"PutItem succeeded: {response}")
                except Exception as e:
                    print(f"Error putting item: {e}")

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Processing completed successfully.',
                    'data': {
                        'table_name': table_name, 
                        'item': item,
                        'datatoput': data
                    }
                })
            }
    else:
              dynamodb.create_table(
                  TableName=table_name,
              KeySchema=[
                  {
                      'AttributeName': 'time',
                      'KeyType': 'HASH' 
                  }
              ],
              AttributeDefinitions=[
                  {
                      'AttributeName': 'time',
                      'AttributeType': 'S' 
                  },
              ],
              ProvisionedThroughput={
                  'ReadCapacityUnits': 10,  
                  'WriteCapacityUnits': 10 
              }
              )
              isexists = dynamodb.get_waiter('table_exists').wait(TableName= table_name)    
              if table_name in isexists:
                table_data = dynamodbres.Table(table_name)
                for record in event['Records']:
                    payload = base64.b64decode(record['kinesis']['data'])
                    data = json.loads(payload)
                    
                    print(f"Data to put: {data}")

                    item = {
                        "time": data["time"],
                        "iteam_id" : data["iteam_id"],
                        "iteam_name":data["iteam_name"],
                        "click_count":data["click_count"]
                    }

                
                    try:
                        response = table_data.put_item(Item=item)
                        print(f"PutItem succeeded: {response}")
                    except Exception as e:
                        print(f"Error putting item: {e}")

                return {
                    'statusCode': 200,
                    'body': json.dumps({
                        'message': 'Processing completed successfully.',
                        'data': {
                            'table_name': table_name, 
                            'item': item,
                            'datatoput': data
                        }
                    })
                }
    

