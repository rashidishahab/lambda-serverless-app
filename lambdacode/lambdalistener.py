import json
import csv
import boto3
import os

def handler(event, context):
    
    region = 'us-east-2'
    record_list=[]
    bucket_name = (os.environ['BUCKET_NAME'])
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        s3 = boto3.client('s3')
        
        dynamodb = boto3.client('dynamodb', region_name = region)
        
        print ('bucket-name: ', bucket_name , 'key:',key)
        
        csv_file = s3.get_object(Bucket = bucket_name, Key = key)
        
        record_list= csv_file['Body'].read().decode('utf-8').split('\n')
        
        csv_reader = csv.reader(record_list, delimiter=',' , quotechar = '"')
        
        for row in csv_reader:
            empid = row[0]
            name = row[1]
            lastname = row[2]
            salary = row[3]
            state = row[4]
            
            add_to_db = dynamodb.put_item(
                TableName = 'employeetable',
                Item = {
                    'empid' : {'N': str(empid)},
                    'name' : {'S': str(name)},
                    'lastname' : {'S': str(lastname)},
                    'salary' : {'S': str(salary)},
                    'status' : {'S': str(state)},
                })
                
            print('Successfully adde CSV record to DynamoDB Table ')
            
    except Exception as e: 
        print (str(e))
           
    return {
        'statusCode': 200,
        'body': json.dumps('CSV to dynamoDB assignment successfully done!')
    }