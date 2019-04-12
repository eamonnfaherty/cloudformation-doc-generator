# product.template
# Description
Enable Guard Duty for every region in your account

## Parameters
The list of parameters for this template:

### AssumableOrgRoleArn 
Type: String   
### TargetOU 
Type: String   
### SpokeIAMPath 
Type: String 
Default: /guardduty-enabler/  
### SpokeIAMRole 
Type: String 
Default: EnablerFunctionRole  
### ScheduleExpression 
Type: String 
Default: None 
Description: Cron or rate expressions to pass through to an AWS::Events::Rule 

## Resources
The list of resources this template creates:

### EnablerFunctionRole 
Type: AWS::IAM::Role  
### EnablerFunction 
Type: AWS::Serverless::Function  
### EnablerFunctionCallerRole 
Type: AWS::IAM::Role  
### EnablerFunctionCusomResource 
Type: AWS::Serverless::Function  
### EnablerFunctionScheduler 
Type: AWS::Serverless::Function  
### SchedulingRule 
Type: AWS::Events::Rule  
### PermissionForEventsToInvokeLambda 
Type: AWS::Lambda::Permission 
Description: PermissionForEventsToInvokeLambda is a lovely lambda 
### Enable 
Type: Custom::CustomResource  

## Outputs
The list of outputs this template exposes:

### PermissionForEventsToInvokeLambda 
Description: Some description about PermissionForEventsToInvokeLambda 
Export name: PermissionForEventsToInvokeLambdaExportedName  

