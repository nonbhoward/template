from constant.names import fn_logger_config, fn_logger_output
from constant.paths import paths
from pathlib import Path
import yaml

# read the configuration
yaml_config = Path(paths['project']['setting'], fn_logger_config)
with open(yaml_config, 'r') as yc:
    logger_configuration = yaml.safe_load(yc)
del yc, yaml_config

# update the logger to use the logging path
logger_configuration['handlers']['file'].update(
    filename=Path(paths['project']['logs'], fn_logger_output))
pass
