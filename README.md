
# A POC using FastAPI, AWS CDK, and Github Actions

This is a practice project aimed to learn how to AWS CDK and Github Actions. A simple api created with FastAPI is at it's core.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

The external packages used in this project can be found in the pyproject.toml file. The requirements.txt file in the root directory are the aws cdk dependencies. The requirements.txt in the src/app directory is used to specify the external python package dependencies to install into the image upon deployment.

The below command will install the aws cdk dependencies.
```
$ pip install -r requirements.txt
```

After that is complete, install the external python dependencies.

```
$ poetry install
```

Active the virtual environment with the below command:

```
% poetry shell
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation