Getting started: https://aws.amazon.com/bedrock/getting-started/

Login to your AWS account from the command line:

```bash
aws configure
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
