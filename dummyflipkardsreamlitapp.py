import streamlit as st
from datetime import datetime
import boto3
import json

session = boto3.Session(
    aws_access_key_id= 'your access key',
    aws_secret_access_key= 'your secret key',
    region_name='your aws region'
)
kinesis_client = session.client("kinesis")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def postUpload(id,name,count):
    try:
            count += 1

            jsondata = {
                "time":current_time,
                "iteam_id" : id,
                "iteam_name":name,
                "click_count":count
                }
            data = json.dumps(jsondata).encode('utf-8')
            print(data)

            responces =   kinesis_client.put_record(
              StreamName="capstone3",
              Data=data,
              PartitionKey="partitionkey"
            )
            print(responces)
            #st.write(data)
    except Exception as e:
        print(e)

st.header("Best Deals On Smartphones")

col1, col2, col3 ,col4 = st.columns(4)

with col1:
    st.header("Google pixel")
    st.image("google_pixel.jpg")
    if st.button(":zap: Buy Now"):
         postUpload('1','google_pixel',1)

with col2:
    st.header("Moto g45")
    st.image("motog45.jpg")
    if st.button(":zap: Buy Now1"):
         postUpload('2','motog45',1)

with col3:
    st.header("RealmeP1")
    st.image("realmeP1.JPG")
    if st.button(":zap: Buy Now2"):
         postUpload('3','realmeP1',1)


with col4:
    st.header("Realmep1Pro")
    st.image("realmep1pro.jpg")
    if st.button(":zap: Buy Now3"):
         postUpload('4','realmep1pro',1)


