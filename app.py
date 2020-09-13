#!/usr/bin/env python3

from aws_cdk import core
from cdk.cdk_stack import CdkStack
from cdk.vpc_stack import VPCStack

import sys

vpc_app = core.App()
VPCStack(vpc_app, "VpcStack", env={'region': 'eu-central-1'}, vpc_name="platformvpc")
vpc_app.synth()


app = core.App()
CdkStack(app, "CdkStack", env={'region': 'eu-central-1'}, queue_name="my_queue")
app.synth()
