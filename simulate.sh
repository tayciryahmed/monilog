rm /tmp/access.log simulation*log
python src/monilog/log_generator.py --rates 9 11 8 --durations 150 150 150 &
python src/monilog/pipeline.py --file /tmp/access.log --threshold 10
