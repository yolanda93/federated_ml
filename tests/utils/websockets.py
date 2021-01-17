from syft.workers.websocket_server import WebsocketServerWorker
from syft.workers.websocket_client import WebsocketClientWorker

def websocket_server_worker(configs, tensor=None):
    """Helper function for spinning up a websocket server"""
    if tensor:
        server_worker = WebsocketServerWorker(
            data=[tensor],
            **configs
        )
    else:
        server_worker = WebsocketServerWorker(
            **configs
        )
    return server_worker


def websocket_client_worker(configs):
    """Helper function for spinning up a websocket client"""
    client_worker = WebsocketClientWorker(
        **configs
    )
    return client_worker