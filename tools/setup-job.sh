#!/bin/sh
set -e

alias hdfs="hadoop/bin/hdfs dfs"

hdfs -mkdir -p user/$(whoami)
hdfs -mkdir -p input
hdfs -mkdir -p src

hdfs -put input/* input
hdfs -put src/* src

hadoop/bin/mapred streaming \
    -input input \
    -output out \
    -mapper src/mapper.py \
    -reducer src/reducer.py

hdfs -cat out/part-00000