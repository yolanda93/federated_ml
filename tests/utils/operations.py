import asyncio
import torch

def check_tensor(worker):
    x_valid = torch.tensor([-1, 2.0]).tag("x")
    x_server = worker.search("x")[0]
    return x_valid, x_server

async def check_tensor(worker):
    x_valid, x_server = check_tensor(worker)
    await asyncio.sleep(0)
    return torch.equal(x_server, x_valid)

async def sum_tensor(worker):
    await asyncio.sleep(0)
    x = torch.ones(5)
    x = x.send(worker)
    y = x + x   # sum operation in server
    y = y.get() # get result from server
    del x
    await asyncio.sleep(2.0)
    return (y == torch.ones(5) * 2).all()

async def add_dataset(worker):
    'TODO'
    return  None

async def train_model(worker):
    'TODO'
    return None