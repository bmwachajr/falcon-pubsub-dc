import falcon
import os
from google.cloud import pubsub_v1

import json
import base64

class PublishResource():
    """ CreateD methods to manage publishing

    """
    def __init__(self):
        self.MESSAGES = []
        self.publisher = pubsub_v1.PublisherClient()

    def on_post(self, req, resp):
        envelope = json.loads(req.media["message"].decode('utf-8'))
        payload = base64.b64decode(envelope['message']['data'])

        self.MESSAGES.append(payload)

        # Returning any 2xx status indicates successful receipt of the message.
        return 'OK', 200

    def on_post_index(self, req, resp):
        data = req.media.get('payload', 'Example payload').encode('utf-8')

        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id="skilful-deck-192907",
            topic='Help_topic',
        )

        try:
            self.publisher.publish(topic_name, data=data)
        except Exception as e:
            raise e

        out = self.publisher.publish(topic_name, data=data)
        
        resp.body = json.dumps({"messagio": "Ding aroooo we all goodie"})
        resp.status = falcon.HTTP_200

    def on_get_index(self, req, resp):
        return self.MESSAGES, 200