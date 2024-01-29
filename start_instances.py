# Function to start ec2 instances
import boto3
import sys
import time


def start_instances(stopped_instances: list):
    ''' Function accepts a list of stopped instances and runs a 
        start instance operation on each instance in the list
    '''
    print(f'\nThese stopped instances will be started: {stopped_instances}')
    decision = input('\nReady to start these instances? (Yes) to proceed, (No) to exit: ').lower()
    while decision != 'yes' :
        if decision != 'no':
            print('\nInvalid Input! Try again')
            decision = input('\nStart instances? (Yes) to proceed, (No) to exit: ').lower()       
        if decision == 'no':
            print('\nExiting operation...')
            sys.exit()
    print('Starting instances')
    ec2_client = boto3.client('ec2')
    response = ec2_client.start_instances(
        InstanceIds=stopped_instances,
        DryRun=False
    )
    time.sleep(3)
    for instance in response['StartingInstances']:
        instance_state = instance['CurrentState']['Name']
        if instance_state == 'pending':
            print(f'\nStarting instance {instance["InstanceId"]}')
        elif instance_state == 'stopped':
            print(f'\nCould not start instance {instance["InstanceId"]}')
        else:
            print(f'\n{instance["InstanceId"]} is already running')


# declare list variable for instances to be started
stopped_ec2 = []


# Call the start function
start_instances(stopped_ec2)
