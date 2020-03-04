rm /tmp/access.log simulation*log
python setup.py install --user
python monilog/bin/run_log_generator.py --rates 9 --durations 30 &
python monilog/bin/run_monitoring.py --file /tmp/access.log --threshold 10
