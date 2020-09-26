import json
import pytest

from aws_cdk import core
from servu-auth.servu_auth_stack import ServuAuthStack


def get_template():
    app = core.App()
    ServuAuthStack(app, "servu-auth")
    return json.dumps(app.synth().get_stack("servu-auth").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
