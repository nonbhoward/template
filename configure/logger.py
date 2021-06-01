from constant.paths import paths
import yaml

# read the configuration
yaml_config = paths['file']['yaml logger config']
with open(yaml_config, 'r') as yc:
    logger_configuration = yaml.safe_load(yc)
del yc, yaml_config

# update the logger to use the logging path
logger_configuration['handlers']['file'].\
    update(filename=paths['file']['logger output'])
pass
