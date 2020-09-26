import boto3
import os

from utils import str_normalizer


if __name__ == '__main__':
    store_name = input('Store Name: ')
    group_name = str_normalizer(store_name)

    client = boto3.client('cognito-idp')
    client.create_group(
        GroupName=group_name,
        UserPoolId=os.getenv('USERPOOL_ID'),
        Description=store_name
    )
