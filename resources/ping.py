import falcon
import json

class PingResource(object):
    """ Ping

    """
    def __init__(self):
        super().__init__()
        
    def on_get(self, req, resp):
        """Handles GET requests
        ---
        summary: Ping the service to check if running
        responses:
            200:
                description: Service is running properly
                content:
                    application/json:
                        schema:
                            $ref: "#/components/schemas/ping"
        """
        output = {
            'name': "falcon pubsub dc",
            'version': "v0.1"
        }

        # Successful response
        resp.body = json.dumps(output)
        resp.status = falcon.HTTP_200
