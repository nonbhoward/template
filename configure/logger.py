from constant.paths import paths
import logging.config
import yaml

# read the configuration
logger_config_file = paths['file']['logger config']
with open(logger_config_file, 'r') as lcf:
    logger_config_dict = yaml.safe_load(lcf)
del lcf, logger_config_file

# direct the logger to use the logging path
logger_config_dict['handlers']['file'].\
    update(filename=paths['file']['logger output'])

# configure the logger
logging.config.dictConfig(logger_config_dict)

# output logger configuration settings
# print(f'configured filename is {}')
# print(f'configured filemode is {}')
# print(f'configured format is {}')
# print(f'configured datefmt is {}')
# print(f'configured level is {}')
