from configure.settings import config, path
from devel.flags import DEBUG
import logging.config

# configure the logger
logging.config.dictConfig(config['logger'])
del config
if DEBUG:
    pass
pass
