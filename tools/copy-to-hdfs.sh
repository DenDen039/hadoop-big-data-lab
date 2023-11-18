#!/bin/sh
set -e

alias hdfs="hadoop/bin/hdfs dfs"

hdfs -mkdir -p /user/$(whoami)
hdfs -mkdir -p input
hdfs -mkdir -p src
hdfs -put input/airlines.csv input
hdfs -put input/flights.csv input
hdfs -put src/* src
