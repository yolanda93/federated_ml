# Private AI - PySyft PoC

## Implemented PoCs

### [virtual workers](virtual_workers/README.md)
Virtual workers are entities present on our local machine. They are used to model the behavior of actual workers.

**01_tricky_operations**
* FECHA: 11/01/2021
* DESCRIPCIÓN: This notebook shows some tricky/advanced tensor operations with PySyft.
* RECURSOS:
  * [Notebook](virtual_workers/01_tricky_operations/01_tricky_operations.ipynb)

**02_fed_nonfed_regression** 
* FECHA: 11/01/2021
* DESCRIPCIÓN: A comparison between PyTorch training and PySyft federated training using virtual workers and a synthetic regression dataset.
* RECURSOS:
  * [Notebook](virtual_workers/02_fed_nonfed_regression/fed_nonfed_simple_regression.ipynb)

### [web sockets](websockets/README.md)

* 1_test_connection: OK
* 2_show_tensor: --
* 3_tensor_sum: OK
* 4_delegated_computation: --
* 5_fed_ml_basic: current
* 
STATUS: Working in PySyft v0.2.5

### [pygrid](pygrid/README.md)

### PoC description

The complete description of the PoCs are in the following doc:
* [PoC pysyft](https://docs.google.com/document/d/1kEfQx9wNfdk32tPyQPq5v6jP5jKsFRvo_6E2JlIJpC0/edit?ts=5f96ffc3)

### PySyft reference docs

* [Websockets PySyft API](https://pysyftbenardi.readthedocs.io/en/add_sphinx_docs/api/syft/workers/index.html)
* [Backlog of reference working examples](https://docs.google.com/spreadsheets/d/1DYnpSa-OpKJ5krIhK_TJ5o2d3C7mg8sEn8ZSeRiWvAQ/edit#gid=0)

### Deployment steps

Substitute with the 'poc_name' with the folder to be launched. e.g. 1b_show_tensor

```console
cd deploy
./launch.sh poc_name 
```

### Run tests 

```python
pytest tests/test_websocket_api.py.py
```

### Presentations

* [Development iterations - executive ppt](https://docs.google.com/presentation/d/1rH7EoaJ9kmRnzF2COQPv8SG91NhGAS_sxIwiicxAoVU/edit#slide=id.gaf99398980_1_129)
