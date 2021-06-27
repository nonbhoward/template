from constant.names import fn_config_logger, fn_log
from constant.paths import path
from pathlib import Path
import yaml

# read the configuration
yaml_config = Path(path.dirs['project']['setting'], fn_config_logger)
with open(yaml_config, 'r') as yc:
    logger_configuration = yaml.safe_load(yc)
del yc, yaml_config

# update the logger to use the logging path
logger_configuration['handlers']['file'].update(
    filename=Path(path.dirs['project']['logs'], fn_log))
pass
