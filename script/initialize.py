from configure.logger import logger_config_dict
import logging.config

# initialize logger, start
# configure the logger
logging.config.dictConfig(logger_config_dict)
# initialize the local logger
log = logging.getLogger(__name__)

# print the logger configuration
print(f'the log level is set to {log.getEffectiveLevel()}')

# test the logger
log.info(f'test info')
log.debug(f'test debug')
log.warning(f'test warning')
log.error(f'test error')
# initialize logger, stop
