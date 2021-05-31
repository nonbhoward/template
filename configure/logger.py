from constant.paths import paths
import yaml

# read the configuration
logger_config_file = paths['file']['logger config']
with open(logger_config_file, 'r') as lcf:
    log_config = yaml.safe_load(lcf)
del lcf, logger_config_file

# direct the logger to use the logging path
log_config['handlers']['file']. \
    update(filename=paths['file']['logger output'])
