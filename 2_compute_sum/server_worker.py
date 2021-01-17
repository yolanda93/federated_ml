from multiprocessing import Process
import syft as sy
from syft.workers.websocket_server import WebsocketServerWorker
import torch
import argparse
import logging

logging.basicConfig( level=logging.INFO, filename='server.log')

local_execution = True

hook = sy.TorchHook(torch)

def exec_pipeline_poc1(socket_pipe):
    a = torch.tensor([1, 2, 3]).tag("a")
    logging.info("SERVER WORKER: Search received tensors:")
    a_server = a.send(socket_pipe)
    logging.info("SERVER WORKER: A: [{}]".format(' '.join(map(str, a_server.numpy()))))

def start_proc(participant, kwargs):
    """ helper function for spinning up a websocket participant """

    def target():
        server = participant(**kwargs)
        server.start()
        exec_pipeline_poc1

    p = Process(target=target)
    p.start()
    logging.info("SERVER WORKER: Running...")
    return p


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run websocket server worker.")

    parser.add_argument(
        "--port", "-p", type=int, help="port number of the websocket server worker, e.g. --port 8777"
    )

    parser.add_argument("--host", type=str, default="localhost", help="host for the connection")

    parser.add_argument(
        "--id", type=str, help="name (id) of the websocket server worker, e.g. --id alice"
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="if set, websocket server worker will be started in verbose mode",
    )

    args = parser.parse_args()
    kwargs = {
        "id": args.id,
        "host": args.host,
        "port": args.port,
        "hook": hook,
    }

    logging.info("SERVER WORKER: Started in host:{}, port:{}".format(kwargs['host'], kwargs['port']))
    server = start_proc(WebsocketServerWorker, kwargs)
    logging.info("SERVER WORKER: Finished")
    server.terminate()

