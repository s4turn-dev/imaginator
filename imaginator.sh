#!/bin/bash

source venv/bin/activate

rows=$(tput lines)
columns=$(tput cols)

python main.py $columns $rows $1 $2 

deactivate
