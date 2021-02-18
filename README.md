# Private AI - PySyft PoC

## Implemented PoCs

### [Virtual Workers](virtual_workers/README.md)
Virtual workers are entities present on our local machine. They are used to model the behavior of actual workers.

**01_tricky_operations**
* DATE: 18/01/2021
* DESCRIPTION: This notebook shows some tricky/advanced tensor operations with PySyft.
* RESOURCES:
  * [Notebook](virtual_workers/01_tricky_operations/notebooks/01_tricky_operations.ipynb)

**02_fed_nonfed_regression** 
* DATE: 25/01/2021
* DESCRIPTION: A comparison between PyTorch training and PySyft federated training using virtual workers and a synthetic regression dataset.
* RESOURCES:
  * [Notebook](virtual_workers/02_fed_nonfed_regression/notebooks/fed_nonfed_simple_regression.ipynb)

### [Web Sockets](websockets/README.md)
Here, each worker is represented by two parts, a local handle (websocket client worker) and the remote instance that holds the data and performs the computations. The remote part is called a websocket server worker.

**01_test_connection**
* DATE: 11/01/2021
* DESCRIPTION: This notebook shows how to stablish a basic websocket connection between a client and a server. 
* RESOURCES:
  * [Notebook](websockets/01_test_connection/notebooks/)

**02_remote_sum**
* DATE: 11/01/2021
* DESCRIPTION: This notebook shows how to implement a remote tensor sum using websockets.
* RESOURCES:
  * [Notebook](websockets/02_remote_sum/notebooks/)

STATUS: Working in PySyft v0.2.5

### [PyGrid](pygrid/README.md)
[PyGrid](https://github.com/OpenMined/PyGrid) is a peer-to-peer network of data owners and data scientists who can collectively train AI models using PySyft. 

**01_data_centric_mnist**
* DATE: 08/02/2021
* DESCRIPTION: This notebook shows how to implement a federated learning following a data centric approach with PyGrid.
* RESOURCES:
  * [Notebook](pygrid/01_data_centric_mnist/notebooks/01_data_centric_mnist.ipynb)

**02_model_centric_regression**
* DATE: 18/02/2021
* DESCRIPTION: This notebook shows how to implement a federated learning following a model centric approach with PyGrid.
* RESOURCES:
  * [Notebook](pygrid/01_model_centric_regression/notebooks/02_model_centric_regression.ipynb)
 

## Reference Documents

The inital draft document with description of the PoCs:
* [PoC pysyft](https://docs.google.com/document/d/1kEfQx9wNfdk32tPyQPq5v6jP5jKsFRvo_6E2JlIJpC0/edit?ts=5f96ffc3)

The description of each sprint iteration:
* [Development iterations - executive ppt](https://docs.google.com/presentation/d/1rH7EoaJ9kmRnzF2COQPv8SG91NhGAS_sxIwiicxAoVU/edit#slide=id.gaf99398980_1_129)

A backlog of working examples found using PySyft:
* [Backlog of reference working examples](https://docs.google.com/spreadsheets/d/1DYnpSa-OpKJ5krIhK_TJ5o2d3C7mg8sEn8ZSeRiWvAQ/edit#gid=0)

#### PySyft reference docs
* [Websockets PySyft API](https://pysyftbenardi.readthedocs.io/en/add_sphinx_docs/api/syft/workers/index.html)


