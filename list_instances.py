import boto3
import sys

def ec2_list_instance(instance_state:list=None):
    '''
    Function returns a list of instance_id's for any state passed as list argument.
    Valid states are: pending, running, shutting-down, terminated, stopping, stopped.
    Defaults to all states if no arguments is passed.
    '''
    if instance_state is None:
        instance_state = ['pending','running','shutting-down','terminated','stopping','stopped']
    else:
        instance_state = [state.lower() for state in instance_state]
        for x in instance_state:
            if x == 'pending' or x == 'running' or x == 'shutting-down' or x == 'terminated' or x == 'stopping' or x == 'stopped':
                continue
            else:
                print('Invalid "state name" passed in function call')
                sys.exit()

    # create an ec2 object using client
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            # dictionary filters in this section. Add more as needed
            {'Name': 'instance-state-name', 'Values': instance_state},
            # {'Name': 'owner-id', 'Values': ['']},
            # {'Name': '', 'Values': []}
            # {'Name': '', 'Values': []}
            # {'Name': 'tag:Name', 'Values': ['serverA','serverB']}
        ],
        # InstanceIds=[],
        DryRun=False,
        MaxResults=100,
        # NextToken='string'
    )
    instance_ids = []
    for obj in response['Reservations']:
        instance_ids.append(obj['Instances'][0]['InstanceId'])
    print(f'\nFound {len(instance_ids)} instances! \n')
    return instance_ids

# Declaring output of function as a variable
stopped_instances = ec2_list_instance(['stopped'])
