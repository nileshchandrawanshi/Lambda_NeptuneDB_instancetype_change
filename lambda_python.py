import boto3

def lambda_handler(event, context):
    neptune_client = boto3.client('neptune')
    
    # List of your Neptune instance identifiers
    neptune_instance_identifiers = ['instance-1', 'instance-2', 'instance-3']  # Add your actual identifiers here
    new_instance_type = 'db.t3.medium'  # Specify your actual NeptuneDB instancetype here

    for identifier in neptune_instance_identifiers:
        try:
            response = neptune_client.modify_db_instance(
                DBInstanceIdentifier=identifier,
                DBInstanceClass=new_instance_type
            )
            print(f"Instance type modification initiated for {identifier}: {response}")
        except Exception as e:
            print(f"Error modifying {identifier}: {e}")
