import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import syft
import torch
from utils.operations import check_tensor, sum_tensor, add_dataset, train_model
from utils.websockets import websocket_server_worker

@pytest.fixture
def local_server():
    hook = syft.TorchHook(torch, verbose=True)
    torch.manual_seed(42)

    x = torch.tensor([-1, 2.0]).tag("x")  # create tensor
    configs = {"host": "localhost", "hook": hook, "verbose": True,
               "port": 'port'}



    return websocket_server_worker(configs=configs, tensor=x)

@pytest.mark.asyncio
async def test_check_tensor(local_server):
    '''
    POC1 - client worker performs a check operation in server worker
    '''
    assert await check_tensor(local_server)

@pytest.mark.asyncio
async def test_sum_tensor(local_server):
    '''
    client worker performs a sum operation in server worker
    '''
    assert await sum_tensor(local_server)

@pytest.mark.asyncio
async def test_add_dataset(local_server):
    '''
    TODO: client worker send a dataset to server worker
    '''
    assert await add_dataset(local_server)

@pytest.mark.asyncio
async def test_train_model(local_server):
    '''
    TODO: client worker train a local model with a remote dataset
    '''
    assert await train_model(local_server)
