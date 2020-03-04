# Monilog

This project allows watching and logging all HTTP traffic of a system, generating log in w3c log format, showing statistics about total requests, maximum hits, requests in a timespan and alerting when traffic is above a customizable threshold.

## Requirements

* Python and preferably Linux.

## Usage
* You can execute `simulate.sh` to run a simulation of how this project works. The simulation setup is customisable, feel free to play with it.

* Make sure to install the package by runing : 

```
python setup.py install 
```

* To run the monitoring in your own log file, run: 

```
monitoring --file /path/to/your/file --threshold 10
```

* To customize the log generation, run: 

```
log_generator --rates 9 11 8 --durations 150 150 150
```

With `rates` being the number of requests per second for each step of the simulation and `durations` being the durations of the corresponding simulation steps.

* To execute the tests , run :

```
nosetests .
```

**Attention:** The monitoring is stopped when no new logs are written to the log
file during `MAX_IDLE_TIME` set by default to 2 minutes. This is added to manage stopping
the monitoring automatically, particularly when doing limited time simulations. 


## Future Improvements
This is a first working solution for http log monitoring. Many improvements can be added : 
* Managing threaded access to the log file using cross-platform file locking. The current implementation is tested on Linux and may
cause errors in Windows. 
* Enhancing the display of the log analysis and statistics. For now, the monitoring results are written 
to standard output and to a log file with the naming convention `simulation-<timestamp>.log`. A better setup would be to customize the 
GUI using [npyscreen](https://pypi.org/project/npyscreen/) for instance. 
* It is also possible to build a live dashboard consuming `simulation-<timestamp>.log` data and mapping it to graphs. 
* Pushing alerting notifications by email or SMS to admins / owners of the monitored system. 
* Adding more relevant statistics to the analysis of the website and handle timezone changes.
* Writing extensive unit and integration tests.
* For a higher scale of data requiring high availability in a production setup, a more robust solution would be indexing the logs in ElasticSearch and building Kibana dashboards, with a stream-processing platform such as Kafka. 
