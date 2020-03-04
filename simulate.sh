pip uninstall -y monilog
rm /tmp/access.log simulation*log
python setup.py install 
log_generator --rates 9 11 8 --durations 150 150 150 &
monitoring --file /tmp/access.log --threshold 10

