import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
group_name = 'all traffic group'
security_group_ids = []
image_id = 'ami-02045ebddb047018b'
instance_type = 't2.micro'
key_name = 'general_keypair'
machine_names = ['master', 'slave']

try:
    # Retrieve security group id
    security_groups = ec2.describe_security_groups()
    security_group_ids = [sg['GroupId'] for sg in security_groups['SecurityGroups']]

    # Create ONE master instance,
    # then create THREE slave instances
    for mn in machine_names:
        max_count, min_count = 0, 0
        if mn == 'master':
            max_count = 1
            min_count = 1

        if mn == 'slave':
            max_count = 3
            min_count = 3

        instance_response = ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            MaxCount=max_count,
            MinCount=min_count,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': mn,
                        }
                    ]
                }
            ]
        )

except ClientError as e:
    print(e)
