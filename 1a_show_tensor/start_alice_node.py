import syft as sy
from syft.workers.websocket_server import WebsocketServerWorker
from syft.workers.websocket_client import WebsocketClientWorker
import torch
import argparse
import logging
import asyncio

logging.basicConfig(level=logging.INFO, filename='../alice.log')
local_execution = True
hook = sy.TorchHook(torch)

async def server_start(participant, kwargs):
    worker = participant(**kwargs)
    await asyncio.sleep(0.1)
    worker.start()
    logging.info("ALICE: Server started")
    await asyncio.sleep(0.1)

async def exec_pipeline_poc1(participant, kwargs):
    kwargs.port += 1
    socket_pipe = participant(**kwargs)
    await asyncio.sleep(0.1)

    logging.info("ALICE: Created local tensors:")
    a = torch.tensor([1, 2, 3]).tag("a")
    logging.info("ALICE: A: [{}]".format(' '.join(map(str, a.numpy()))))

    a.send(socket_pipe)
    logging.info("ALICE: Sent tensor to remote node")
    await asyncio.sleep(0.1)


def start_tasks_workers(server_kwargs, client_kwargs):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        server_start(WebsocketServerWorker, server_kwargs),
        exec_pipeline_poc1(WebsocketClientWorker, client_kwargs),
    ))
    loop.close()


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

    logging.info("ALICE: Started in host:{}, port:{}".format(kwargs['host'], kwargs['port']))
    start_tasks_workers(kwargs)
    logging.info("ALICE: Finished")
