# **Spelling Corrector**
This repo is a spelling corrector that I forked from Peter Norvigs project on his [website](http://norvig.com/spell-correct.html).
I have added below how you can deploy the same project in using lambda and attaching an API endpoint to it in the AWS cloud. You can follow the steps below on how to setup the code using 
inside of a lambda and attach an endpoint.

The notebooks repo has an example of the code that has been implemented and how the backend (spelling corrector) logic works. 

### Step 1: Zip up the following files that are present in the Project Repo
- 7z a Spelling_Corrector.zip lambda_function.py big.txt Utilities.py

### Step 2: Creating IAM Role for your lambda**
You need to create your IAM role sourcing the role document from the Project repo, the file is called lambda_role.json

- aws iam create-role --role-name Spelling-Correct-Role --assume-role-policy-document file://lambda_role.json

### Step 3: Creating the lambda function
In here, firstly you need to get the arn of your role to a variable and then pass it as a parameter while you create your lambda function along with your zipped file that you had done in Step 1

- aws lambda create-function --function-name Spelling_Corrector --runtime python3.8 --handler lambda_function.lambda_handler --timeout 300  --role ${Role_arn} --zip-file fileb://Spelling_Corrector.zip

### Step 4: Creating your API endppoint
Lets first create the API endpoint
- aws apigatewayv2 create-api --name spelling-api-sample --protocol-type HTTP --route-key "GET /word" --target ${LAMBDA_ARN}

## Step 5: Giving your API trigger the permission to invoke the lambda as a resource role
This is a bit sticky (and I was lazy to get the API_ARN so I had to frame it myself, firstly we need to get some variables in, so you would need to run the folliwng commands in order:
- ACCOUNT_NUMBER=(**Insert your account number**)
- API_ID=$(aws apigatewayv2 get-apis | jq '.[]|.[]|.ApiId' | tr -d '"')

Next you would need to frame your API_ARN string, run the following git bash commands
- API_ARN="arn:aws:execute-api:us-east-1:ACCOUNT_NUMBER:API_ID/*/*/word"

Substituting your ACCOUNT_NUBMER and API_ID in the API_ARN
- API_ARN=${API_ARN/ACCOUNT_NUMBER/${ACCOUNT_NUMBER}}
- API_ARN=${API_ARN/API_ID/${API_ID}

Finally attaching the resource role to your lambda
- aws lambda add-permission --statement-id 1 --action lambda:InvokeFunction --function-name ${LAMBDA_ARN} --principal apigateway.amazonaws.com --source-arn ${API_ARN}

## Step 6: Invoking your endpoint
You can now trigger your lambda using your api endpoint (which you can get using your console, you need to replace your url here, add your resource and the querystring, which is the input word of which you want to see the correction)
- curl https://oqzcb6to2d.execute-api.us-east-1.amazonaws.com/word?somthing

You can also try the same using your browser using the images below
