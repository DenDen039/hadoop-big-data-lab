# Hadoop lab

## Setup project

1. Copy dataset `airlines.csv` and `flights.csv` to `./input` dir. If you don't have dataset you can download it [here](https://www.kaggle.com/datasets/usdot/flight-delays/download?datasetVersionNumber=1)
2. Get hadoop using:
```
$ wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
$ tar -xf hadoop-3.3.6.tar.gz && mv hadoop-3.3.6 hadoop
``` 
3. Inside `hadoop/etc/hadoop/hadoop-env.sh` change parameter based on JAVA setup. Example:
```
# set to the root of your Java installation
export JAVA_HOME=/usr/java/latest
```
4. Install `openssh` package.
5. Launch `sshd` server.
6. Using this [instruction](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html). 
Complete necessary steps: `Pseudo-Distributed Operation -> Configuration, Setup passphraseless ssh`.
7. Format hadoop file system: 
```
$ hadoop/bin/hdfs namenode -format
```
8. Start NameNode daemon and DataNode daemon:
```
$ hadoop/sbin/start-dfs.sh
```
9. Run job script by:
```
$ ./tools/setup-job.sh
```