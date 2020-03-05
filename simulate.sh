rm /tmp/access.log 

pip install monilog==0.1.3 

log_generator --rates 8 12 8 --durations 150 150 150 &
monitoring --file /tmp/access.log --threshold 10


