from configure.settings import config
from configure.settings import path
import logging.config
logging.config.dictConfig(config['logger'])
