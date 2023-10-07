#!/bin/bash
if [ "$#" -lt 1 ]; then
    conda install --file ./requirments.txt

else
    ENV_NAME=$1
    if $(conda info --envs | grep -q "$ENV_NAME"); then
        echo "$ENV_NAME already exits!"
    else
        conda create --name $ENV_NAME
        conda activate $ENV_NAME
    fi
    conda install --file ./requirments.txt
fi