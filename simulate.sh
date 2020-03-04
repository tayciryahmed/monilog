rm /tmp/access.log simulation*log
python setup.py install 
log_generator --rates 9 --durations 30 &
monitoring --file /tmp/access.log --threshold 10

