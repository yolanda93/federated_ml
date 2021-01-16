from multiprocessing import Process
import syft as sy
from syft.workers.websocket_client import WebsocketClientWorker
import torch
import argparse
import logging
import time
logging.basicConfig( level=logging.INFO, filename='client.log')

local_execution = True

hook = sy.TorchHook(torch)


def exec_pipeline(socket_pipe):
    a = torch.tensor([1, 2, 3]).tag("a")
    b = torch.tensor([3, 2, 1]).tag("b")
    logging.info("CLIENT WORKER: Created local tensors:")
    logging.info("CLIENT WORKER: A: [{}]".format(' '.join(map(str, a.numpy()))))
    logging.info("CLIENT WORKER: B: [{}]".format(' '.join(map(str, b.numpy()))))

    a_at_server = a.send(socket_pipe)
    b_at_server = b.send(socket_pipe)
    logging.info("CLIENT WORKER: Sent tensor to remote node BOB")

    c_at_server = a_at_server + b_at_server
    logging.info("CLIENT WORKER: Computed sum on remote node")

    c_at_local = c_at_server.get()
    logging.info("CLIENT WORKER: Get the result to local, removing from remote")
    logging.info("CLIENT WORKER: Final result: [{}]".format(' '.join(map(str, c_at_local.numpy()))))


def start_proc(participant, kwargs):
    """ helper function for spinning up a websocket participant """

    def target():
        socket_pipe = participant(**kwargs)
        logging.info("CLIENT WORKER: Connected")
        exec_pipeline(socket_pipe)


    p = Process(target=target)
    p.start()

    return p


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
    "verbose": args.verbose,
}

kwargs_2 = {"id": "fed", "host": "localhost", "port": 8768, "hook": hook}

if local_execution:
    logging.info("CLIENT WORKER: Local mode")
    start_proc(WebsocketClientWorker, kwargs_2)
else:
    logging.info("CLIENT WORKER: Remote mode")
    socket_pipe = WebsocketClientWorker(**kwargs)
    exec_pipeline(socket_pipe)

