1. Clonar repo:
git clone https://github.com/OpenMined/PyGrid
conda create -n pygrid python=3.7
conda activate pygrid
pip install poetry
poetry install

**2. Levantar network: **
$ cd PyGrid/apps/network
$ ./run.sh --port 7000 --start_local_db

3. Levantar nodos:
$ cd PyGrid/apps/node
$ ./run.sh --id bob --port 5000 --start_local_db --host 0.0.0.0 --network http://0.0.0.0:7000

Endpoints utiles:

NODO
http://0.0.0.0:5000/data-centric/identity
http://0.0.0.0:5000/data-centric/status
http://0.0.0.0:5000/data-centric/models
http://0.0.0.0:5000/data-centric/workers

RED
http://0.0.0.0:7000/connected-nodes
http://0.0.0.0:7000/search-available-tags

Scripts de test:
https://drive.google.com/drive/folders/134BSz9CHP4BpIKxQc0sE_0tsIJ6p7vCs?usp=sharing