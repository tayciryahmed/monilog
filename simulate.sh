rm /tmp/access.log
python src/monilog/log_generator.py &
python src/monilog/pipeline.py