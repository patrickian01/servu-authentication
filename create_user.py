import boto3
import os

from datetime import datetime
from utils import str_normalizer


if __name__ == '__main__':
    email = input('E-mail: ')
    store_name = input('Store: ')

    client = boto3.client('cognito-idp')
    client.admin_create_user(
        UserPoolId=os.getenv('USERPOOL_ID'),
        Username=email
    )

    client.admin_add_user_to_group(
        UserPoolId=os.getenv('USERPOOL_ID'),
        Username=email,
        GroupName=str_normalizer(store_name)
    )
