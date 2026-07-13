Getting started: https://aws.amazon.com/bedrock/getting-started/

Login to your AWS account from the command line:

```bash
aws login --profile your-profile-name
```

Set the default profile for the current session:

```bash
export AWS_PROFILE=your-profile-name
```

Install python packages:

pip:

```bash
    pip install "anthropic[bedrock]" boto3 "botocore[crt]"
```

uv:

```bash
    uv add "anthropic[bedrock]" boto3 "botocore[crt]"
```
