FROM python:3.7

ARG WORKER_ID 
ENV WORKER_ID ${WORKER_ID}

RUN echo "installing ${WORKER_ID}"

# set up working directory in the container
ENV WORKSPACE /1b_show_tensor
WORKDIR $WORKSPACE

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./src./
RUN mkdir $WORKSPACE/log_files

EXPOSE 8768 
