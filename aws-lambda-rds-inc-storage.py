from __future__ import print_function
import boto3
import json

cw = boto3.client('cloudwatch')
rds = boto3.client('rds')

def lambda_handler(event, context):
    response = cw.describe_alarms(
        StateValue='ALARM',
        AlarmNamePrefix='awsrds',
    )
    for alarm in response['MetricAlarms']:
        if alarm['MetricName'] == 'FreeStorageSpace':
            database = alarm['Dimensions'][0]['Value']
            response = rds.describe_db_instances(
                DBInstanceIdentifier=database,
            )
            AllocatedStorage = (response['DBInstances'][0]['AllocatedStorage'])
            # is necessary increase minimum 10% of storage 
            NewStorage = int(((AllocatedStorage)*0.10)+(AllocatedStorage)+1)
            response = rds.modify_db_instance(
                DBInstanceIdentifier=database,
                AllocatedStorage=NewStorage,
                ApplyImmediately=True,
            )
            print(response)
