#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_poc.cdk_poc_stack import CdkPocStack
from cdk_poc.pipeline_stack import PipelineStack

app = cdk.App()
CdkPocStack(app, "CdkPocStack",
    env={
        'account': '156161676080',
        'region': 'eu-central-1',
    }
)

CdkPocStack(app, "CdkPocStack-Brazil",
    env={
        'account': '156161676080',
        'region': 'sa-east-1',
    }
)

PipelineStack(app, 'PipelineStack', env={
        'account': '156161676080',
        'region': 'eu-central-1',
    }
)

app.synth()
