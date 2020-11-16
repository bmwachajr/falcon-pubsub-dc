import falcon
from resources.publish import PublishResource
from resources.subscribe import SubscribeResource
from resources.ping import PingResource

def create():
    api = falcon.API()

    # Resources
    publish_resource = PublishResource()
    subscribe_resource = SubscribeResource()
    ping_resource = PingResource()

    # Reoutes
    api.add_route('/ping', ping_resource)
    api.add_route('/publish', publish_resource)
    api.add_route('/publish/index', publish_resource, suffix='index')



    return api

api = create()
