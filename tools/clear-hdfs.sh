#!/bin/sh
set -e

hadoop/bin/hdfs dfs -rm -r -f /user/$(whoami)