Setup
=====

This is for the local machine aka your laptop/desktop, not EC2 VM. The local machine should have Ubuntu-family distros.

## AWS CLI 2

```shell
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Run [`aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Boto3

```shell
pip install boto3
```

Generate
========

## AWS CLI 2 EC 2

Create keypair

```shell
aws ec2 create-key-pair --key-name general_keypair --query 'KeyMaterial' --output text > secrets/general_keypair.pem
```

[Amazon EC 2 Keypairs](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html)

Create
======

## Security Group

```shell
python experiments/create_security_group.py
```

## 1 Master and 3 Slaves

```shell
python experiments/create_t2micro.py
```