import builtins
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as _alambda,
)


class AnimeQuoteGeneratorService(Construct):
    def __init__(self, scope: Construct, id: builtins.str) -> None:
        super().__init__(scope, id)

        handler = _alambda.PythonFunction(
            self,
            "AnimeQuoteGeneratorHandler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            entry="./resources",
            index="anime_quote_generator.py",
            handler="handler",
        )

        api = apigateway.RestApi(
            self,
            "AnimeQuoteGeneratorApi",
            rest_api_name="Anime Quote Generator Service",
            description="This service serves anime quotes",
        )

        anime_quote_generator_integration = apigateway.LambdaIntegration(
            handler, request_templates={"application/json": '{ "statusCode": "200" }'}
        )
        api.root.add_method("GET", anime_quote_generator_integration)  # Get /
