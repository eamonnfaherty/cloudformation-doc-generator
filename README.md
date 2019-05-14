# What is this?

Installing this tool will provide you with the command ```cfn-docs```.

The command ```cfn-docs``` accepts an AWS CloudFormation template and returns a description of the 
template in markdown:

```bash
cfn-docs org-bootstrap.template.yaml > org-bootstrap.template.README.md
```

In the example above we redirect the std out into a file.

## What does it read?
The tool will read the description from the template, each parameter, each resource and each output.  It will output
those descriptions in a markdown document under suitable headers.  It also lists parameters, resources and outputs 
that do not have any descriptions.