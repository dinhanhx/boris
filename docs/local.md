Setup
=====

This setup for the local machine aka your laptop/desktop, not EC2 VM. The local machine should have Ubuntu-family distros.

All of these commands are executed at the root folder of this project AKA where the main/first readme.md stays.

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

All of these commands are executed at the root folder of this project AKA where the main/first readme.md stays.

These commands MUST be executed on the local machine aka your laptop/desktop, not EC2 VM. The local machine should have Ubuntu-family distros.

## Security Group

```shell
python experiments/create_security_group.py
```

## 1 Master and n Slaves

```shell
python experiments/create_t2micro.py
```

For example, if you want 4 slaves, change `number_slave = 1` to `number_slave = 4`.

## K8S

```shell
python experiments/generate_cmds.py > setup_cmds.sh
# Maybe you should copy and paste each line then run one by one in setup_cmds.sh 
bash setup_cmds.sh
```


