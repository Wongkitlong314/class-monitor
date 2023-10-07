#!/bin/bash
CONDA_BASE=$(conda info --base)
source "$CONDA_BASE"/etc/profile.d/conda.sh
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
    
    echo -e "\nFinished! The new environment name is $ENV_NAME "
    echo -e "\nTo activate the environment use:\n\n\tconda activate $ENV_NAME"
fi