from aws_cdk import (
    aws_dynamodb as _dynamodb,
    aws_iam as _iam,
    aws_s3 as _s3,
    aws_s3_notifications as _s3_notify,
    aws_lambda as _lambda,
    core
)


class CdkShahabStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        my_table  = _dynamodb.Table( self, id = 'dynamoTable', table_name='employeetable'
                                    ,partition_key= _dynamodb.Attribute(name='empid', type= _dynamodb.AttributeType.NUMBER ))
                                    
        my_bucket = _s3.Bucket(self, 's3bucket', bucket_name='employeebucket-assignment')

        lambda_func = _lambda.Function( self, 'shahabassignmentfunction', runtime=_lambda.Runtime.PYTHON_3_7, 
                                        handler= 'lambdalistener.handler', code = _lambda.Code.asset('lambdacode'),
                                        environment={'BUCKET_NAME':
                                                        my_bucket.bucket_name}
                                      ) 
       # Create trigger for Lambda function using suffix
        notification = _s3_notify.LambdaDestination(lambda_func)
        notification.bind(self, my_bucket)
        
        # Add Create Event only for .csv files
        my_bucket.add_object_created_notification(
           notification, _s3.NotificationKeyFilter(suffix='.csv'))
           
           