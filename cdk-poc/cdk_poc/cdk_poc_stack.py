from os import path
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw


from aws_cdk import (
    Stack,
    CfnOutput
)
from constructs import Construct

class CdkPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        handler_a = lmb.Function(self, 'HandlerA',
            runtime=lmb.Runtime.PYTHON_3_9,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda_a'))
        )

        handler_b = lmb.Function(self, 'HandlerB',
            runtime=lmb.Runtime.PYTHON_3_9,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda_b'))
        )

        handler_c = lmb.Function(self, 'HandlerC',
            runtime=lmb.Runtime.PYTHON_3_9,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda_c'))
        )

        gw = apigw.LambdaRestApi(self, 'Gateway',
            description="POC CDK lambda",
            handler=handler_a.current_version,
        )


        self.url_output = CfnOutput(self, 'Url',
            value=gw.url
        )
