from aws_cdk import (
    core,
    aws_lambda as _lambda,
)


class LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, tykSecret, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            vpc=vpc,
            handler='main.handler',
            environment={
                "TYK_SECRET": tykSecret
            }
        )