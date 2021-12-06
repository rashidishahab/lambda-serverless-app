
# General description 

This project has been developed over Cloud9 instance, just to make you sure the that i can use Cloud9 as well as development environment.

I used aws CDK for development and deployment.

tech stack used are follows as below : </br>

1) aws S3 
2) aws DynamoDB
3) aws lambda 
4) aws notifier

stack written in python [cd_shahab_stack.py] and the lambda function also written in python. 

The lambda function is triggered when a csv file uplod to the S3 bucket "employeebucket-assignment". the CSV file sample created and located in the project directory "employee.csv" once the csv file uploaded to the S3 bucket the lambda functioned will be called and handler start to get the object from the S3 bucket "employeebucket-assignment" and read to import into the DynamoDB "employeetable". with aws cloud watch i coud monitor logs group ==> "2021/12/06/[$LATEST]6763536a805244d4a976417b70c701b9"
```sh
2021-12-06T14:19:01.600+03:00
bucket-name:  employeebucket-assignment key: employee.csv
	bucket-name: employeebucket-assignment key: employee.csv
2021-12-06T14:19:02.030+03:00
Successfully adde CSV record to DynamoDB Table 
	Successfully adde CSV record to DynamoDB Table  
```
#  CDK Python project for lambda serverless function !

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`cdk_shahab_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
# serverles-lambda-cdk-assignment
