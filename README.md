# **Spelling Corrector**
This repo is a spelling corrector that I forked from Peter Norvigs project on his [website](http://norvig.com/spell-correct.html).
I have added below how you can deploy the same project in using lambda and attaching an API endpoint to it in the AWS cloud. You can follow the steps below on how to setup the code using 
inside of a lambda and attach an endpoint.

The notebooks repo has an example of the code that has been implemented and how the backend (spelling corrector) logic works. 

**Step 1: Zip up the following files that are present in the Project Repo**
- 7z a Spelling_Corrector.zip lambda_function.py big.txt Utilities.py

**Step 2**: Creating IAM Role for your lambda
You need to create your IAM role sourcing the role document from the Project repo, the file is called lambda_role.json
- aws iam create-role --role-name Spelling-Correct-Role --assume-role-policy-document file://lambda_role.json


