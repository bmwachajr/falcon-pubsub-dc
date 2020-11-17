import os
from google.cloud import pubsub_v1

def callback(message):
    print(message.data)
    message.ack()

class SubscribeResource():
    """ CreateD methods to manage publishing

    """
    def __init__(self):
        self.subscriber = pubsub_v1.SubscriberClient()

        self.topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id="skilful-deck-192907",
            topic='Help_topic',
        )

        self.subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
            project_id="skilful-deck-192907",
            sub='sub_one',  # Set this to something appropriate.
        )

    def on_get(self, req, resp):
        try:
            future = self.subscriber.subscribe(self.subscription_name, callback)
            future.result()
        except Exception as e:
            future.cancel()
            raise e

        breakpoint()