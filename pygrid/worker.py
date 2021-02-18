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

results = my_smart_grid.search("#Test")
print("Results: ", str(results))


#get pointer to first result
ds_tensor_ptr=results.get(list(results.keys())[0])[0]

def sum_column(dataset, column):
    sum_result = dataset[0][column].copy()
    for i in range(1, dataset.shape[0]):
        sum_result += dataset[i][column]
    return sum_result

#compute remotely the sum of the column
result_ptr=sum_column(ds_tensor_ptr, 1)


print("Column result:"+str(result_ptr.get()))

