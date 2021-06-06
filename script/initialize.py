from configure.logger import logger_configuration, paths
from devel.flags import DEBUG
import logging.config

# configure the logger
logging.config.dictConfig(logger_configuration)
del logger_configuration
if DEBUG:
    pass
pass
