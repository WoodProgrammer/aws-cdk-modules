from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,  vpc_name, **kwargs) -> None:

        super().__init__(scope, id, **kwargs)
        self.vpc_new = ec2.Vpc(self, vpc_name, cidr="10.0.0.0/16")
        

    def getVpcObject(self):
        return self.vpc_new
