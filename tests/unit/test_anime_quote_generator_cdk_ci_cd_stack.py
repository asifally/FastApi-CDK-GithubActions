import aws_cdk as core
import aws_cdk.assertions as assertions

from anime_quote_generator_cdk_ci_cd.anime_quote_generator_cdk_ci_cd_stack import AnimeQuoteGeneratorCdkCiCdStack

# example tests. To run these tests, uncomment this file along with the example
# resource in anime_quote_generator_cdk_ci_cd/anime_quote_generator_cdk_ci_cd_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AnimeQuoteGeneratorCdkCiCdStack(app, "anime-quote-generator-cdk-ci-cd")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
