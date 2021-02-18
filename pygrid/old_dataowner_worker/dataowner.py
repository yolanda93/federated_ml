import torch as th
import syft as sy
import time
from syft.grid.clients.data_centric_fl_client import DataCentricFLClient
hook = sy.TorchHook(th)

nodeBob = DataCentricFLClient(hook, id="Bob", address="ws://bob:5000")
nodeAlice = DataCentricFLClient(hook, id="Alice", address="ws://alice:5001")

data_description = """Description:
                        Bob test data.
                        Columns:
                            Example 1: Boolean
                            Example 2: Float
                            Example 3: Float
                    """

data_description_2 = """Description:
                        Bob production data.
                        Columns:
                            Example 1: Boolean
                            Example 2: Float
                            Example 3: Float
                    """

example_data = th.tensor([[1, 3.5, 62.3],
                          [0, 32.4, 234.2],
                          [0, 92.4, 9.4],
                          [1, 452.9, 123.9],
                          [0, 12.9, 19.4]])

example_data_2 = th.tensor([[1, 23.1, 62.3],
                          [0, 32.4, 24.2],
                          [0, 92.4, 94.4],
                          [1, 45.9, 123.9],
                          [0, 126.9, 19.4]])

example_data_2.tag("#Test", "#Data").describe(data_description_2)
example_data.tag("#Test", "#Data2").describe(data_description)

data_pointer = example_data_2.send(nodeBob)
data_pointer_2 = example_data.send(nodeAlice)

print("-------------------------------------")
print("DATOS PUBLICADOS POR LOS NODOS")
print("-------------------------------------")
print("")

bob_search = nodeBob.search("#Test")
alice_search = nodeAlice.search("#Test")
print(bob_search)
print(alice_search)

while(True):
    time.sleep(20)
    print(alice_search)
    print(bob_search)
