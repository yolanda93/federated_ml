import torch as th
import syft as sy
import time
#import regressionDataset
#import pandas
from syft.grid.clients.data_centric_fl_client import DataCentricFLClient
hook = sy.TorchHook(th)

nodeBob = DataCentricFLClient(hook, id="bob", address="ws://0.0.0.0:5000")
nodeAlice = DataCentricFLClient(hook, id="alice", address="ws://0.0.0.0:5001")


#train_set = regressionDataset.RegressionDataset(csv_file="data/data.csv",root_dir="data")

#federated_train_loader = sy.FederatedDataLoader(train_set.federate((alice, bob)), batch_size=15, shuffle=True)


data_description = """Description:
                        Bob test data.
                        Columns:
                            Example 1: Boolean
                            Example 2: Float
                            Example 3: Float
                    """
data_description_alice = """Description:
                        Alice test data.
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

example_data_alice = th.tensor([[1, 3.5, 62.3],
                          [0, 32.4, 234.2],
                          [0, 92.4, 9.4],
                          [1, 452.9, 123.9],
                          [0, 12.9, 19.4]])
example_data_2 = th.tensor([[1, 23.1, 62.3],
                          [0, 32.4, 24.2],
                          [0, 92.4, 94.4],
                          [1, 45.9, 123.9],
                          [0, 126.9, 19.4]])

example_data_2.tag("#Test", "#BOB").describe(data_description_2)
example_data.tag("#Test", "#BOB2").describe(data_description)
example_data_alice.tag("#Test", "#ALICE").describe(data_description_alice)

data_pointer = example_data_2.send(nodeBob, user="bob")
#data_pointer_2 = example_data.send(nodeBob, user="bob")
data_pointer_alice = example_data_alice.send(nodeAlice, user="alice")

print("-------------------------------------")
print("DATOS PUBLICADOS POR ALICE")
print("-------------------------------------")
print("")

something = nodeBob.search("#Test")
print(something)

while(True):
    time.sleep(20)
     print(something)
