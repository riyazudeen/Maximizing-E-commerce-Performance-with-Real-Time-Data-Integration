# Maximizing-E-commerce-Performance-with-Real-Time-Data-Integration
As an e-commerce company, our success hinges on seamlessly integrating our online platform with efficient logistics management to ensure optimal customer satisfaction and operational efficiency. To achieve this synergy, we aim to leverage real-time data streams from both our website and fleet of delivery trucks. 

## Steps 
* I have created dummy streamlit app there i have place a 4 product images and buynow button
* when user click the buynow  the product detail like id,name,count of the click will will be get by kinesis stream data
* then the data will processed and uploaded to dynamodb.
* the truck iot detail like speed of truck,temp and ect (it's a dummy truck iot detail) pass to ApiGate (post method)
* from that data process by lambda function and uploaded to dynamodb


## Technology used in this project
 * Python
 * Boto3
 * API Gateway
 * AWS Kinesis
 * AWS Lambda Function
 * AWS DynamoD
