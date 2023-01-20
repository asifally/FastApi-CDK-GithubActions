from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import anime_quote_generator_service

class AnimeQuoteGeneratorCdkCiCdStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        anime_quote_generator_service.AnimeQuoteGeneratorService(self, "AnimeQuoteGenerator")
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AnimeQuoteGeneratorCdkCiCdQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
