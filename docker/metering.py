import boto3
import os
import logging

logging.basicConfig(level=logging.INFO)

client = boto3.client('meteringmarketplace')
client.meta.region_name


def registerUsage():
    try:
        product_code = 'Our_Product_code'
        response = client.register_usage(
            ProductCode=product_code,
            PublicKeyVersion=1
        )
        logging.info('Response from RegisterUsage API call '+str(response))
        print('Usage registered successfully!')
        return True
    except Exception as e:
        logging.error("Error could not call registerusage api **" + str(e))
        print('Error registering usage: {}'.format(e))
        return False

registerUsage()
