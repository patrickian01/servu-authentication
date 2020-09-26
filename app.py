#!/usr/bin/env python3
import os

from aws_cdk import core
from servu_auth.servu_auth_stack import ServuAuthStack


app = core.App()
ServuAuthStack(app, 'servu-authentication', env={'region': os.getenv('AWS_REGION')})

app.synth()
