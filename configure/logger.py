from constant.paths import paths
import yaml

# read the configuration
yaml_config = paths['file']['yaml logger config']
with open(yaml_config, 'r') as yc:
    config_for_log = yaml.safe_load(yc)
del yc, yaml_config

# direct the logger to use the logging path
config_for_log['handlers']['file'].\
    update(filename=paths['file']['logger output'])
pass
