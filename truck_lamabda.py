import json
import boto3

AWS_ACCESS_KEY_ID = 'your aws key ID'
AWS_SECRET_ACCESS_KEY = 'your aws access key'
session = boto3.Session(
    aws_access_key_id= AWS_ACCESS_KEY_ID,
    aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
    region_name='add your region'
)

def lambda_handler(event, context):
     dynamodb = session.client('dynamodb')
     dynamodbres = session.resource('dynamodb')
     table_name = 'truckData'
     isexisits = dynamodb.list_tables()['TableNames']
     if table_name in isexisits:
                 count = 0
                 if isinstance(event, str):
                  jsonevent = json.loads(event)
                 table_data = dynamodbres.Table(table_name)
                 truckload = jsonevent
                 for i in truckload["trucks"]:
                    timeData = i["time"]
                    truckData = i["truck_data"]
                    today=i["date"]
                    dicl={
                            "time":timeData,
                            "date":today,
                            "truck_data":truckData
                        }
                    count += 1
                    table_data.put_item(Item=dicl)
                 return {
                       'statusCode': 200,
                       'body': json.dumps({'result': "Data uploaded!",
                      }),
                      'jsone':jsonevent,
                      'count':count
                    } 
     else:
              
              dynamodb.create_table(
                          TableName=table_name,
              KeySchema=[
                  {
                      'AttributeName': 'time',
                      'KeyType': 'HASH'  
                  },

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

              if isexists:
                 table_data = dynamodbres.Table(table_name)
                 if isinstance(event, str):
                  jsonevent = json.loads(event)
                 truckload = jsonevent
                 for i in truckload["trucks"]:
                    timeData = i["time"]
                    truckData = i["truck_data"]
                    today=i["date"]
                    dicl={
                            "time":timeData,
                            "date":today,
                            "truck_data":truckData
                        }
                    table_data.put_item(Item=dicl)
                 return {
                       'statusCode': 200,
                       'body': json.dumps({'result': "Data uploaded!",
                      }),
                      'jsone':jsonevent
                    }  
              else:
                   return {
                       'statusCode': 200,
                       'body': json.dumps({'result': "No Data uploaded!",
                      })
                    } 
                 
               
          
