from constant.paths import paths
import yaml

# read the configuration
logger_config_file = paths['file']['logger config']
with open(logger_config_file, 'r') as lcf:
    logger_config_dict = yaml.safe_load(lcf)
del lcf, logger_config_file

# direct the logger to use the logging path
logger_config_dict['handlers']['file'].\
    update(filename=paths['file']['logger output'])
