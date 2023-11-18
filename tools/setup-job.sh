#!/bin/sh
set -e

hadoop/bin/mapred streaming \
    -input input \
    -output out \
    -mapper src/mapper.py \
    -reducer src/reducer.py
clear
hadoop/bin/hdfs dfs -cat out/part-00000