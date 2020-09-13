from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_ec2 as ec2,
    aws_sns_subscriptions as subs,
    core
)



class CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,  queue_name, **kwargs) -> None:
        self.name_check = self.check_name_of_queue(queue_name)

        super().__init__(scope, id, **kwargs)

        if self.name_check == True:

            queue = sqs.Queue(
                self, queue_name,
                visibility_timeout=core.Duration.seconds(300),
            )

            topic = sns.Topic(
                self, "CdkTopic"
            )

            topic.add_subscription(subs.SqsSubscription(queue))
        else:
            print("Check your queue name pls")
            exit(1)
    
    def check_name_of_queue(self, name):
        if "my" in name :
            return False
        else:
            return True

