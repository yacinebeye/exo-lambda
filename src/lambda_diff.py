import logging 

import boto3 

logging.basicConfig(level=logging.INFO)
logger = logging.getlogger()
logger.setLevel(logging.INFO)

ec2_client = boto3.client("ec2")


def handler(event, context):
    ****This function should cleanup unattached network interfaces
    describe nifs 
    deleted unattached
    ****
    raise NotImplementedError
    logger.info("Initialising NIF cleanup process...")
    response = ec2_client.describe_network_interfaces(
      Filters=[
        { 
            "Name": "status", 
            "Values": [
                  "available",
            ]
        }
      ]      
    )
    nif_ids = [nif["NetworkInterfaceId"] for nif in reponse["NetworkInterfaces"]]
    for nif_id in nif_ids:
      ec2_client.delete_network_interface(nif_id)
      logger.info(f"NIF {nif_id} been deleted")
    