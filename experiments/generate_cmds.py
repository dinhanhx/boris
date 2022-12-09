import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ])

machines = {'master': None,
            'slave': []}

for i in response['Reservations']:
    instance = i['Instances'][0]
    public_dns_name = instance['PublicDnsName']

    if instance['Tags'][0]['Value'] == 'master':
        machines['master'] = {'PublicDnsName': instance['PublicDnsName']}
    if instance['Tags'][0]['Value'] == 'slave':
        machines['slave'].append({'PublicDnsName': instance['PublicDnsName']})

    print(f'scp -i secrets/general_keypair.pem experiments/10-kubeadm.conf ubuntu@{public_dns_name}:/home/ubuntu/')

print(f"ssh -i secrets/general_keypair.pem ubuntu@{machines['master']['PublicDnsName']} 'sudo bash -s' < experiments/master.sh")
print(f"scp -i secrets/general_keypair.pem ubuntu@{machines['master']['PublicDnsName']}:/home/ubuntu/join.sh secrets/")

for slave in machines['slave']:
    print(f"scp -i secrets/general_keypair.pem secrets/join.sh ubuntu@{slave['PublicDnsName']}:/home/ubuntu/")
    print(f"ssh -i secrets/general_keypair.pem ubuntu@{slave['PublicDnsName']} 'sudo bash -s' < experiments/slave.sh")

print(f"ssh -i secrets/general_keypair.pem ubuntu@{machines['master']['PublicDnsName']} 'sudo bash -s' < experiments/create_webapp.sh")