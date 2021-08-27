# Graph

# This is for my own personal learning and interest. Hope it will be useful for others who might need it.

# Setup
1. Ensure you have set up a S3 Bucket with the data you want to read from
2. Ensure you have set up Athena to query your data from the S3 bucket
3. Ensure you have set up another S3 Bucket so that later on Lambda can export your graph to that S3 bucket
4. Ensure that you have set permission correctly so that the services such as S3,Athena and Lambda are able to get and put properly

# AWS Lambda
1. Create a function called 'Graph' with runtime python 3.8
2. Edit graph.py accordingly
3. Create a layer in AWS Lambda ( Look for 'Layers' under 'Additional Resoucres' on the left side ) for matplotlib and upload the matplotlib_layer.zip
4. Deploy and Run the function. You will be able to find an output png called 'schoolResult.png in your S3 Bucket for graph
5. Tip: If the creation of graph needed more time to be created, under 'Configuration' set your Timeout to 5 min.
