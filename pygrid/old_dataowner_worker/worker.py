import torch as th
import syft as sy
from syft.grid.clients.data_centric_fl_client import DataCentricFLClient
hook = sy.TorchHook(th)

my_smart_grid = sy.PublicGridNetwork(hook, "http://0.0.0.0:7000")

print("")
print("-------------------------------------")
print("DATOS PEDIDOS A LA GRID CON TAG TEST")
print("-------------------------------------")
print("")


print("Results: ")
print(my_smart_grid.search())
