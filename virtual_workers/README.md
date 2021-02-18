### Installation instructions

#### Option 1: Using the Helper script

If you want to build an experiment run the following:
```console
cd deploy
./launch.sh create poc_folder_name # e.g. ./launch.sh create 01_tricky_operations 
```

If you want to run an already created image:
```console
cd deploy
./launch.sh run poc_folder_name # e.g. ./launch.sh run 01_tricky_operations 
```


#### Option 2: Using Docker instructions

Alternatively, you can create the docker image without the help of any script:

```console
docker build -t poc_folder_name . # e.g. .docker build -t 01_tricky_operations 
docker run -it poc_folder_name /sh/bin
```

Probably, you might want to mount a local folder, so notebooks changes are saved locally.

```console
docker run -it --rm -v ./01_tricky_operations/notebooks:/workspace/notebooks 01_tricky_operations /sh/bin 
```
