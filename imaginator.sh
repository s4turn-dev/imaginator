#!/bin/bash

rows=$(tput lines)
columns=$(tput cols)

python main.py $columns $rows $1 $2 
