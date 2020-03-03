# Monilog

This project allows watching and logging all HTTP traffic of a system, generating log in w3c log format, showing statistics about total requests, maximum hits, requests in a timespan and alerting when traffic is above a customizable threshold.

## Requirements

* Python and preferably Linux.

## Usage
* You can execute `simulate.sh` to run a simulation of how this project works. The simulation setup is customisable, feel free to play with it.
* To run the monitoring in your own log file, run: 

```
python src/monilog/pipeline.py --file /path/to/your/file --threshold 10
```

* To customize the log generation, run: 

```
python src/monilog/log_generator.py --rates 9 11 8 --durations 150 150 150
```

With `rates` being the number of requests per second for each step of the simulation and `durations` being the durations of the corresponding simulation steps.


## Future Improvements
This is a first working solution for http log monitoring. Many improvements can be added : 
* Managing threaded access to the log file using cross-platform file locking. The current implementation is tested on Linux and may
cause errors in Windows. 
* Enhancing the display of the log analysis and statistics. For now, the monitoring results are written 
to standard output and to a log file with the naming convention `simulation-<timestamp>.log`. A better setup would be to customize the 
GUI using [npyscreen](https://pypi.org/project/npyscreen/) for instance. It is also possible to build a live dashboard consuming `simulation-<timestamp>.log` data and mapping it to graphs. 
* Pushing alerting notifications by email or SMS to admins / owners of the monitored system. 
* Adding more relevant statistics to the analysis of the website and handle timezone changes.
* For a higher scale of data requiring high availability in a production setup, a more robust solution would be indexing the logs in ElasticSearch and building Kibana dashboards, with a stream-processing platform such as Kafka. 
