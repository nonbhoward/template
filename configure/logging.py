from constant.paths import paths
import yaml
logger_config_file = paths['file']['logger config']
with open(logger_config_file, 'r') as lcf:
    contents = lcf.read()
pass
# TODO configure logger
# planned data flow..
#   1. yaml text on disk
#   2. yaml load to dict
#   3. logging.dictConfig read
