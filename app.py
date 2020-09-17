#!/usr/bin/env python3

from aws_cdk import core
from cdk.cdk_stack import CdkStack
from cdk.vpc_stack import VPCStack
from cdk.serverless_stack import LambdaStack
from cdk.secret_utils import secrets

if __name__ == "__main__":

    app = core.App()
    secretOut = secrets.getSecret()
    vpcObj = VPCStack(app, "VpcStack", env={'region': 'eu-central-1'}, vpc_name="platformvpc").getVpcObject()
    LambdaStack(app, "LambdaStack", env={'region': 'eu-central-1'}, vpc=vpcObj, tykSecret=secretOut)

    app.synth()