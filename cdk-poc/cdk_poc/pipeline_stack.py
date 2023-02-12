from aws_cdk import (
    Stack,
    CfnOutput,
    SecretValue
)

from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub(
                                "mvlbarcelos/poc-aws-lambda", 
                                "setup",
                                authentication=SecretValue.secrets_manager("github")
                            ),
                            commands=[
                                "npm install -g aws-cdk",
                                "python -m pip install -r cdk-poc/requirements.txt",
                                "cdk synth"
                            ]
                        )
                    )