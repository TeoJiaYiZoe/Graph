import json
import numpy as np
from matplotlib import pyplot as plt 
import io
import boto3
import time
import numpy as np


# Querying from S3
query = 'select * FROM <DATABASE>' # Input your athena database name

DATABASE = <DATABASE> # Input your athena database name
output= <S3 BUCKET URL> # Input your S3 bucket URL so that you can find your output static graph

def lambda_handler(event, context):

    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': output,
        }
    )
    # Observe results
    queryId = response['QueryExecutionId']
    print("Response QueryId: ", queryId)
    # To allow athena to finish running
    time.sleep(5)
    results = client.get_query_results(QueryExecutionId=queryId)
    # Reading your dataset in athena
    for row in results['ResultSet']['Rows']:
        print(row) #output is in dict format
    
    # Data to be replaced using your output from above. This is just a sample data.
    x1 = ['math', 'english', 'science', 'Hindi', 'social studies']
    y1 = [92, 54, 63, 75, 53]
    
    # Plotting the Data
    plt.plot(x1, y1, label='School Semester')
    plt.xlabel('subjects')
    plt.ylabel('marks')
    plt.title("marks obtained in 2010")
  
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('BUCKET-NAME') # Put in S3 bucket. Replace name
    bucket.put_object(Body=img_data,ContentType='image/png', Key='schoolResult.png') # You can name the image as you like eg result.png