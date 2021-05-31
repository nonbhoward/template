from configure.logger import config_for_log
from devel.flags import DEBUG
import logging.config

# configure the logger
logging.config.dictConfig(config_for_log)
del config_for_log

# get some loggers
logr = logging.getLogger()
log = logging.getLogger(__name__)

if DEBUG:
    # test root logger
    print(f'testing the root logger')
    logr.debug(f'root logger test debug message')
    logr.info(f'root logger test info message')
    logr.warning(f'root logger test warning message')
    logr.error(f'root logger test error message')
    # test module logger
    print(f'testing the module logger')
    log.debug(f'module logger test debug message')
    log.info(f'module logger test info message')
    log.warning(f'module logger test warning message')
    log.error(f'module logger test error message')
pass
